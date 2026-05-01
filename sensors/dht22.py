# sensors/dht22.py

import time
import Adafruit_DHT


class DHT22Sensor:
    """
    Kapselt den Zugriff auf einen AM2302 / DHT22 Sensor.
    Liest Temperatur und Luftfeuchte robust aus und puffert
    den letzten gültigen Messwert.
    """

    def __init__(self, gpio_pin):
        self.sensor = Adafruit_DHT.DHT22
        self.pin = gpio_pin

        self.temperature = None  # °C
        self.humidity = None     # %
        self.last_update = None  # Unix-Timestamp

    def read(self):
        """
        Versucht, den Sensor auszulesen.
        Gibt True zurück, wenn ein gültiger Wert gelesen wurde.
        Gibt False zurück bei Fehler (alte Werte bleiben erhalten).
        """

        humidity, temperature = Adafruit_DHT.read_retry(
            self.sensor,
            self.pin,
            retries=3,
            delay_seconds=2
        )

        # Gültige Werte prüfen
        if humidity is not None and temperature is not None:
            self.temperature = round(temperature, 1)
            self.humidity = round(humidity, 1)
            self.last_update = time.time()
            return True

        return False