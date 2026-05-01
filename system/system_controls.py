# system/system_controls.py

import tkinter as tk
import os
import sys
import config

from system.cleanup import cleanup


def open_system_menu(root, leds):
    """
    Modales System-Menü mit sauberem Cleanup.
    """

    popup = tk.Toplevel(root)
    popup.title("System")
    popup.geometry("300x260")
    popup.configure(bg=config.BG_COLOR)
    popup.transient(root)
    popup.grab_set()

    label = tk.Label(
        popup,
        text="System-Menü",
        font=config.FONT_MEDIUM,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR,
    )
    label.pack(pady=20)

    def close_kiosk():
        popup.destroy()
        cleanup(leds)
        root.destroy()
        sys.exit(0)

    def reboot():
        popup.destroy()
        cleanup(leds)
        os.system("sudo reboot")

    def shutdown():
        popup.destroy()
        cleanup(leds)
        os.system("sudo shutdown -h now")

    tk.Button(
        popup,
        text="Kiosk verlassen",
        font=config.FONT_SMALL,
        width=20,
        command=close_kiosk,
    ).pack(pady=5)

    tk.Button(
        popup,
        text="Neustart",
        font=config.FONT_SMALL,
        width=20,
        command=reboot,
    ).pack(pady=5)

    tk.Button(
        popup,
        text="Herunterfahren",
        font=config.FONT_SMALL,
        width=20,
        command=shutdown,
    ).pack(pady=5)

    tk.Button(
        popup,
        text="Abbrechen",
        font=config.FONT_SMALL,
        width=20,
        command=popup.destroy,
    ).pack(pady=15)