# ui/weather_update.py
import config


ICON_MAP = {
    "01": "☀",
    "02": "🌤",
    "03": "☁",
    "04": "☁",
    "09": "🌧",
    "10": "🌦",
    "11": "⛈",
    "13": "❄",
    "50": "🌫"
}


def icon_from_code(code):
    return ICON_MAP.get(code[:2], "☁")


def update_weather(root, weather, today_label, tomorrow_label):
    success = weather.fetch()

    if success and weather.today and weather.tomorrow:
        t = weather.today
        m = weather.tomorrow

        today_label.config(
            text=f"{icon_from_code(t['icon'])} Heute  {t['temp']} °C\n{t['text']}"
        )
        tomorrow_label.config(
            text=f"{icon_from_code(m['icon'])} Morgen {m['temp']} °C\n{m['text']}"
        )
    else:
        today_label.config(text="🌐 Keine Wetterdaten")
        tomorrow_label.config(text="")

    root.after(
        config.WEATHER_UPDATE_INTERVAL * 1000,
        update_weather,
        root,
        weather,
        today_label,
        tomorrow_label,
    )