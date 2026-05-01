# ui/lighting_controls.py
import tkinter as tk
import config


def build_lighting_controls(parent, leds):
    """
    Erzeugt die komplette Beleuchtungs-UI
    und bindet sie an den NeoPixelController.
    """

    frame = tk.Frame(parent, bg=config.BG_COLOR)
    frame.pack(fill="x", pady=10)

    # --- EIN / AUS ---
    power_frame = tk.Frame(frame, bg=config.BG_COLOR)
    power_frame.pack(pady=5)

    on_button = tk.Button(
        power_frame,
        text="EIN",
        font=config.FONT_MEDIUM,
        width=8,
        command=leds.on
    )
    on_button.pack(side="left", padx=10)

    off_button = tk.Button(
        power_frame,
        text="AUS",
        font=config.FONT_MEDIUM,
        width=8,
        command=leds.off
    )
    off_button.pack(side="left", padx=10)

    # --- Helligkeit ---
    brightness_label = tk.Label(
        frame,
        text="Helligkeit",
        font=config.FONT_SMALL,
        fg=config.FG_COLOR,
        bg=config.BG_COLOR
    )
    brightness_label.pack(pady=(10, 0))

    def on_brightness_change(value):
        leds.set_brightness(float(value) / 100)

    brightness_slider = tk.Scale(
        frame,
        from_=0,
        to=100,
        orient="horizontal",
        length=500,
        showvalue=True,
        command=on_brightness_change,
        bg=config.BG_COLOR,
        fg=config.FG_COLOR,
        troughcolor="#444",
        highlightthickness=0
    )
    brightness_slider.set(int(config.NEOPIXEL_BRIGHTNESS * 100))
    brightness_slider.pack(pady=5)

    # --- Farb-Presets ---
    color_frame = tk.Frame(frame, bg=config.BG_COLOR)
    color_frame.pack(pady=10)

    tk.Button(
        color_frame,
        text="❄ Kaltweiß",
        font=config.FONT_SMALL,
        width=10,
        command=lambda: leds.set_color(config.COLOR_COLD)
    ).pack(side="left", padx=5)

    tk.Button(
        color_frame,
        text="☀ Warmweiß",
        font=config.FONT_SMALL,
        width=10,
        command=lambda: leds.set_color(config.COLOR_WARM)
    ).pack(side="left", padx=5)

    tk.Button(
        color_frame,
        text="🕯 Amber",
        font=config.FONT_SMALL,
        width=10,
        command=lambda: leds.set_color(config.COLOR_AMBER)
    ).pack(side="left", padx=5)

    return frame