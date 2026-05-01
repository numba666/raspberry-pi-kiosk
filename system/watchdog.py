# system/watchdog.py
import time
import sys


class SoftwareWatchdog:
    """
    Einfacher Software-Watchdog mit Heartbeat-Prinzip.
    """

    def __init__(self, timeout_seconds):
        self.timeout = timeout_seconds
        self.last_heartbeat = time.time()

    def kick(self):
        """
        Signalisiert: System lebt.
        """
        self.last_heartbeat = time.time()

    def check(self):
        """
        Prüft, ob der Watchdog ausgelöst werden muss.
        """
        if time.time() - self.last_heartbeat > self.timeout:
            print("WATCHDOG: Timeout - System reagiert nicht mehr.")
            sys.exit(1)  # systemd übernimmt