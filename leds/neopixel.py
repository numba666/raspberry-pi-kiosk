# leds/neopixel.py

from rpi_ws281x import PixelStrip, Color


class NeoPixelController:
    def __init__(self, led_count, gpio_pin, brightness):
        self.led_count = led_count
        self.brightness = brightness
        self.is_on = False
        self.current_color = (0, 0, 0)

        self.strip = PixelStrip(
            led_count,
            gpio_pin,
            brightness=int(brightness * 255),
            auto_write=False
        )
        self.strip.begin()

        self.clear()

    def _apply_color(self, color):
        r, g, b = color
        for i in range(self.led_count):
            self.strip.setPixelColor(i, Color(r, g, b))
        self.strip.show()

    def set_color(self, color):
        self.current_color = color
        if self.is_on:
            self._apply_color(color)

    def set_brightness(self, brightness):
        """
        brightness: 0.0 – 1.0
        """
        self.brightness = max(0.0, min(1.0, brightness))
        self.strip.setBrightness(int(self.brightness * 255))
        if self.is_on:
            self._apply_color(self.current_color)

    def on(self):
        self.is_on = True
        self._apply_color(self.current_color)

    def off(self):
        self.is_on = False
        self.clear()

    def clear(self):
        for i in range(self.led_count):
            self.strip.setPixelColor(i, Color(0, 0, 0))
        self.strip.show()