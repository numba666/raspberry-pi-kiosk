# system/cleanup.py
import sys


def cleanup(leds=None):
    """
    Führt einen sauberen Shutdown-Cleanup durch.
    """
    print("CLEANUP: Starte sauberen Shutdown...")

    # LEDs ausschalten
    if leds is not None:
        try:
            leds.off()
            print("CLEANUP: LEDs ausgeschaltet")
        except Exception as e:
            print("CLEANUP: Fehler beim LED-Off:", e)

    print("CLEANUP: abgeschlossen")
