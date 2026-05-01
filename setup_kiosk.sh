#!/bin/bash

# =====================================================
# KIOSK SETUP SCRIPT
# =====================================================
# Dieses Script:
#  - aktualisiert das System
#  - installiert alle benötigten Pakete
#  - installiert Python-Libraries
#  - richtet das Projektverzeichnis ein
#  - legt den systemd-Kiosk-Service an
#  - aktiviert den Hardware-Watchdog-Treiber
#
# Bewusst NICHT automatisiert:
#  - systemd RuntimeWatchdogSec (manuell erklären!)
#
# Philosophy:
#  - Transparent
#  - Reproduzierbar
#  - Embedded-tauglich
# =====================================================

set -e  # Bei Fehler sofort abbrechen

echo "============================"
echo " Kiosk Setup wird gestartet "
echo "============================"

# -----------------------------------------------------
# 1. System aktualisieren
# -----------------------------------------------------
echo "▶ System aktualisieren..."
sudo apt update
sudo apt upgrade -y

# -----------------------------------------------------
# 2. Benötigte Systempakete
# -----------------------------------------------------
echo "▶ Installiere Systempakete..."

sudo apt install -y \
    python3 \
    python3-pip \
    python3-tk \
    python3-rpi-ws281x \
    git \
    curl \
    watchdog

# watchdog-Paket ist nicht zwingend nötig,
# aber nützlich für Diagnose & Tests.

# -----------------------------------------------------
# 3. Python Dependencies
# -----------------------------------------------------
echo "▶ Installiere Python-Pakete..."

pip3 install --upgrade pip
pip3 install Adafruit_DHT requests

# -----------------------------------------------------
# 4. Projektverzeichnis vorbereiten
# -----------------------------------------------------
PROJECT_DIR="/home/pi/kiosk"

echo "▶ Stelle Projektverzeichnis sicher: $PROJECT_DIR"
sudo mkdir -p "$PROJECT_DIR"
sudo chown pi:pi "$PROJECT_DIR"

# -----------------------------------------------------
# 5. systemd Kiosk-Service anlegen
# -----------------------------------------------------
SERVICE_FILE="/etc/systemd/system/kiosk.service"

echo "▶ Erstelle systemd Service: kiosk.service"

sudo tee "$SERVICE_FILE" > /dev/null <<EOF
[Unit]
Description=Kiosk UI
After=network.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/kiosk
ExecStart=/usr/bin/python3 /home/pi/kiosk/main.py
Restart=always
RestartSec=5
Environment=DISPLAY=:0
Environment=XAUTHORITY=/home/pi/.Xauthority

[Install]
WantedBy=multi-user.target
EOF

# -----------------------------------------------------
# 6. systemd aktivieren
# -----------------------------------------------------
echo "▶ Aktiviere systemd Service..."
sudo systemctl daemon-reload
sudo systemctl enable kiosk.service

# -----------------------------------------------------
# 7. Hardware-Watchdog (Kernel-Ebene)
# -----------------------------------------------------
echo "▶ Aktiviere Hardware-Watchdog (bcm2835_wdt)..."

# Modul einmal laden
sudo modprobe bcm2835_wdt

# Dauerhaft beim Boot laden
if ! grep -q "bcm2835_wdt" /etc/modules; then
    echo "bcm2835_wdt" | sudo tee -a /etc/modules > /dev/null
    echo "▶ Watchdog-Modul zu /etc/modules hinzugefügt"
else
    echo "▶ Watchdog-Modul bereits eingetragen"
fi

# -----------------------------------------------------
# Abschluss
# -----------------------------------------------------
echo ""
echo "============================"
echo " ✅ Setup abgeschlossen!"
echo "============================"
echo ""
echo "👉 Nächste manuelle Schritte (BEWUSST):"
echo ""
echo "1) systemd Hardware-Watchdog aktivieren:"
echo "   sudo nano /etc/systemd/system.conf"
echo ""
echo "   Dort setzen:"
echo "     RuntimeWatchdogSec=15"
echo "     ShutdownWatchdogSec=10"
echo ""
echo "2) Danach laden:"
echo "   sudo systemctl daemon-reexec"
echo ""
echo "3) Projektdateien nach /home/pi/kiosk kopieren"
echo "4) Starten mit:"
echo "   sudo systemctl start kiosk.service"
echo ""
echo "Reboot optional – empfohlen nach Watchdog-Setup."