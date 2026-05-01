# main.py
#
# Zentrale Orchestrierung der Kiosk-Anwendung
#

import tkinter as tk
import random

import config

# --- UI ---
from ui.layout import build_layout
from ui.clock import update_clock
from ui.sensor_update import update_sensor
from ui.lighting_controls import build_lighting_controls
from ui.weather_update import update_weather

# --- Hardware ---
from sensors.dht22 import DHT22Sensor
from leds.neopixel import NeoPixelController

# --- System ---
from system.pin_dialog import request_pin, is_pin_locked
from system.system_controls import open_system_menu
from system.watchdog import SoftwareWatchdog

# --- Weather ---
from weather.openweather import OpenWeather

# --- UI Statusfarben ---
COLOR_NORMAL = config.FG_COLOR
COLOR_LOCKED = "#888888"   # ruhiges Grau
``


def load_quote():
    try:
        with open("quotes.txt", "r", encoding="utf-8") as f:
            quotes = [line.strip() for line in f if line.strip()]
        return random.choice(quotes)
    except Exception:
        return "Willkommen."


def main():
    # --------------------------------------------------
    # Tkinter Basis / Kioskmodus
    # --------------------------------------------------
    root = tk.Tk()
    root.title("Kiosk")

    root.geometry(f"{config.SCREEN_WIDTH}x{config.SCREEN_HEIGHT}")
    root.configure(bg=config.BG_COLOR)

    root.attributes("-fullscreen", True)
    root.config(cursor="none")

    # --------------------------------------------------
    # Layout
    # --------------------------------------------------
    (
        quote_label,
        time_label,
        date_label,
        temp_label,
        hum_label,
        weather_today_label,
        weather_tomorrow_label,
        bottom_frame,
    ) = build_layout(root)

    quote_label.config(text=load_quote())

    # --------------------------------------------------
    # Uhr & Datum
    # --------------------------------------------------
    update_clock(root, time_label, date_label)

    # --------------------------------------------------
    # Sensoren
    # --------------------------------------------------
    dht_sensor = DHT22Sensor(config.DHT_GPIO)
    update_sensor(root, dht_sensor, temp_label, hum_label)

    # --------------------------------------------------
    # Neopixel
    # --------------------------------------------------
    leds = NeoPixelController(
        led_count=config.NEOPIXEL_COUNT,
        gpio_pin=config.NEOPIXEL_GPIO,
        brightness=config.NEOPIXEL_BRIGHTNESS,
    )
    leds.set_color(config.COLOR_WARM)
    leds.on()

    # --------------------------------------------------
    # Wetter
    # --------------------------------------------------
    weather = OpenWeather(
        api_key=config.WEATHER_API_KEY,
        lat=config.WEATHER_LAT,
        lon=config.WEATHER_LON,
        lang=config.WEATHER_LANG,
    )

    update_weather(
        root,
        weather,
        weather_today_label,
        weather_tomorrow_label,
    )

    # --------------------------------------------------
    # Lichtsteuerung
    # --------------------------------------------------
    build_lighting_controls(bottom_frame, leds)

    # --------------------------------------------------
    # System-Button (⚙) mit PIN
    # --------------------------------------------------
    system_button = tk.Button(
        bottom_frame,
        text="⚙",
        font=config.FONT_MEDIUM,
        width=3,
        command=lambda: request_pin(
            root,
            lambda: open_system_menu(root, leds),
        ),
    )
    system_button.pack(side="right", padx=20)

    # --------------------------------------------------
    # Statusanzeige für PIN-Cooldown (rechts neben ⚙)
    # --------------------------------------------------
    status_label = tk.Label(
        bottom_frame,
        text="",
        font=config.FONT_SMALL,
        fg="gray",
        bg=config.BG_COLOR,
    )
    status_label.pack(side="right", padx=10)

    # --------------------------------------------------
    # Sichtbare Sicherheit: Status regelmäßig aktualisieren
    # --------------------------------------------------
def update_system_button():
    locked, remaining = is_pin_locked()

    if locked:
        system_button.config(text="🔒", fg=COLOR_LOCKED)
        status_label.config(text=f"{remaining}s", fg=COLOR_LOCKED)
    else:
        system_button.config(text="⚙", fg=COLOR_NORMAL)
        status_label.config(text="", fg=COLOR_NORMAL)

    root.after(1000, update_system_button)

    update_system_button()

    # --------------------------------------------------
    # Software-Watchdog
    # --------------------------------------------------
    watchdog = SoftwareWatchdog(timeout_seconds=30)

    def watchdog_heartbeat():
        watchdog.kick()
        watchdog.check()
        root.after(5000, watchdog_heartbeat)

    watchdog_heartbeat()

    # --------------------------------------------------
    # Mainloop
    # --------------------------------------------------
    root.mainloop()


if __name__ == "__main__":
    main()