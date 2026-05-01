# system/pin_dialog.py

import tkinter as tk
import time
import config

# --------------------------------------------------
# Interner Zustand (lokal im PIN-Modul)
# --------------------------------------------------
_failed_attempts = 0
_locked_until = 0


def request_pin(root, on_success):
    """
    Öffnet einen modalen PIN-Dialog.
    Führt Fehlversuch-Zählung und Cooldown durch.
    """

    global _failed_attempts, _locked_until

    now = time.time()

    # --------------------------------------------------
    # Prüfen: PIN aktuell gesperrt?
    # --------------------------------------------------
    if now < _locked_until:
        remaining = int(_locked_until - now)
        _show_locked_message(root, remaining)
        return

    popup = tk.Toplevel(root)
    popup.title("PIN benötigt")
    popup.geometry("300x220")
    popup.configure(bg=config.BG_COLOR)
    popup.transient(root)
    popup.grab_set()

    label = tk.Label(
        popup,
        text="Bitte PIN eingeben",
        font=config.FONT_MEDIUM,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR,
    )
    label.pack(pady=15)

    pin_var = tk.StringVar()

    entry = tk.Entry(
        popup,
        textvariable=pin_var,
        font=config.FONT_MEDIUM,
        show="*",
        justify="center",
    )
    entry.pack(pady=5)
    entry.focus_set()

    status_label = tk.Label(
        popup,
        text="",
        font=config.FONT_SMALL,
        fg="red",
        bg=config.BG_COLOR,
    )
    status_label.pack(pady=5)

    def check_pin():
        nonlocal popup
        global _failed_attempts, _locked_until

        if pin_var.get() == config.SYSTEM_PIN:
            _failed_attempts = 0
            popup.destroy()
            on_success()
            return

        # --- falscher PIN ---
        _failed_attempts += 1
        pin_var.set("")

        remaining = config.PIN_MAX_ATTEMPTS - _failed_attempts

        if remaining > 0:
            status_label.config(
                text=f"Falscher PIN ({remaining} Versuche übrig)"
            )
        else:
            _locked_until = time.time() + config.PIN_COOLDOWN_SECONDS
            _failed_attempts = 0
            popup.destroy()
            _show_locked_message(root, config.PIN_COOLDOWN_SECONDS)

    tk.Button(
        popup,
        text="OK",
        font=config.FONT_SMALL,
        width=10,
        command=check_pin,
    ).pack(pady=5)

    tk.Button(
        popup,
        text="Abbrechen",
        font=config.FONT_SMALL,
        width=10,
        command=popup.destroy,
    ).pack(pady=5)


# --------------------------------------------------
# Status-Abfrage für UI (nur lesen, keine Logik!)
# --------------------------------------------------
def is_pin_locked():
    """
    Gibt zurück:
    (True, Restsekunden) wenn gesperrt,
    (False, 0) sonst
    """
    now = time.time()
    if now < _locked_until:
        return True, int(_locked_until - now)
    return False, 0


# --------------------------------------------------
# Interne Lock-Meldung
# --------------------------------------------------
def _show_locked_message(root, remaining_seconds):
    popup = tk.Toplevel(root)
    popup.title("Gesperrt")
    popup.geometry("300x160")
    popup.configure(bg=config.BG_COLOR)
    popup.transient(root)
    popup.grab_set()

    label = tk.Label(
        popup,
        text=(
            "Zu viele Fehlversuche\n"
            f"Bitte {remaining_seconds} Sekunden warten"
        ),
        font=config.FONT_SMALL,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR,
        justify="center",
    )
    label.pack(pady=30)

    tk.Button(
        popup,
        text="OK",
        font=config.FONT_SMALL,
        width=10,
        command=popup.destroy,
    ).pack()