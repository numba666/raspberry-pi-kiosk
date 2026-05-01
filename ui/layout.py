# ui/layout.py
import tkinter as tk
import config


def build_layout(root):
    root.configure(bg=config.BG_COLOR)

    # =====================================================
    # Obere Leiste: Spruch links, Uhr & Datum rechts
    # =====================================================
    top = tk.Frame(root, bg=config.BG_COLOR, height=120)
    top.pack(fill="x")

    # --- Spruch des Tages ---
    quote_label = tk.Label(
        top,
        text="",
        font=config.FONT_MEDIUM,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR,
        wraplength=600,
        justify="left"
    )
    quote_label.pack(side="left", padx=20, pady=20, anchor="w")

    # --- Uhr & Datum ---
    clock_frame = tk.Frame(top, bg=config.BG_COLOR)
    clock_frame.pack(side="right", padx=20, pady=10, anchor="e")

    time_label = tk.Label(
        clock_frame,
        text="",
        font=config.FONT_LARGE,
        fg=config.ACCENT_COLOR,
        bg=config.BG_COLOR
    )
    time_label.pack(anchor="e")

    date_label = tk.Label(
        clock_frame,
        text="",
        font=config.FONT_SMALL,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR
    )
    date_label.pack(anchor="e")

    # =====================================================
    # Mittlerer Bereich: links Sensoren, rechts später Wetter
    # =====================================================
    middle = tk.Frame(root, bg=config.BG_COLOR)
    middle.pack(expand=True, fill="both", padx=20)

    # --- Links: Temperatur & Luftfeuchte ---
    left = tk.Frame(middle, bg=config.BG_COLOR)
    left.pack(side="left", expand=True, anchor="n")

    temp_label = tk.Label(
        left,
        text="🌡 --.- °C",
        font=config.FONT_LARGE,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR
    )
    temp_label.pack(anchor="w", pady=(20, 5))

    hum_label = tk.Label(
        left,
        text="💧 --.- %",
        font=config.FONT_LARGE,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR
    )
    hum_label.pack(anchor="w")

 
    # --- Rechts: Wetter ---
    right = tk.Frame(middle, bg=config.BG_COLOR)
    right.pack(side="right", expand=True, anchor="n")

    weather_today = tk.Label(
        right,
        text="🌐 Wetter lädt …",
        font=config.FONT_MEDIUM,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR,
        justify="left"
    )
    weather_today.pack(anchor="e", pady=(20, 10))

    weather_tomorrow = tk.Label(
        right,
        text="",
        font=config.FONT_SMALL,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR,
        justify="left"
    )
    weather_tomorrow.pack(anchor="e")

    return (
        quote_label,
        time_label,
        date_label,
        temp_label,
        hum_label,
        weather_today,
        weather_tomorrow,
        bottom
    )

    # =====================================================
    # Unterer Bereich: Lichtsteuerung
    # =====================================================
    bottom = tk.Frame(root, bg=config.BG_COLOR, height=150)
    bottom.pack(fill="x")

    # =====================================================
    # Rückgabe aller benötigten UI-Elemente
    # =====================================================
    return (
        quote_label,
        time_label,
        date_label,
        temp_label,
        hum_label,
        bottom
    )