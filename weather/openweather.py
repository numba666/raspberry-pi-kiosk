# weather/openweather.py
import requests
import time


class OpenWeather:
    """
    Schlankes OpenWeather-Modul:
    - Holt Vorhersage
    - Extrahiert HEUTE & MORGEN
    """

    BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

    def __init__(self, api_key, lat, lon, lang="de"):
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.lang = lang

        self.today = None
        self.tomorrow = None
        self.last_update = None

    def fetch(self):
        params = {
            "lat": self.lat,
            "lon": self.lon,
            "appid": self.api_key,
            "units": "metric",
            "lang": self.lang
        }

        try:
            response = requests.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()

            self._parse(data)
            self.last_update = time.time()
            return True

        except Exception:
            return False

    def _parse(self, data):
        """
        OpenWeather liefert 3h-Blöcke.
        Wir nehmen:
        - ersten Eintrag = heute
        - Eintrag +24h ≈ morgen
        """
        entries = data.get("list", [])

        if len(entries) < 9:
            return

        self.today = self._extract(entries[0])
        self.tomorrow = self._extract(entries[8])

    def _extract(self, entry):
        return {
            "temp": round(entry["main"]["temp"]),
            "icon": entry["weather"][0]["icon"],
            "text": entry["weather"][0]["description"].capitalize()
        }