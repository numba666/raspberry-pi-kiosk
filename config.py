# config.py


DHT_GPIO = 4

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 480

BG_COLOR = "#1e1e1e"
FG_COLOR = "#f0f0f0"
ACCENT_COLOR = "#ffb000"

FONT_LARGE = ("DejaVu Sans", 36)
FONT_MEDIUM = ("DejaVu Sans", 24)
FONT_SMALL = ("DejaVu Sans", 16)

# config.py

SYSTEM_PIN = "1234"

PIN_MAX_ATTEMPTS = 3
PIN_COOLDOWN_SECONDS = 30

# --- Neopixel ---
NEOPIXEL_GPIO = 18        # PWM-fähiger Pin
NEOPIXEL_COUNT = 100      # später einfach erhöhen
NEOPIXEL_BRIGHTNESS = 0.4 # Maximal 40 % (stromsparend)

COLOR_COLD = (255, 255, 240)
COLOR_WARM = (255, 180, 100)
COLOR_AMBER = (255, 120, 0)

# --- Wetter ---
WEATHER_API_KEY = "DEIN_OPENWEATHER_API_KEY"
WEATHER_LAT = 47.0471
WEATHER_LON = 15.1533

WEATHER_UPDATE_INTERVAL = 3600  # Sekunden (1 Stunde)
WEATHER_LANG = "de"
