# raspberry-pi-kiosk
A calm, resilient Raspberry Pi kiosk system with embedded-first design.


# Raspberry Pi Kiosk System
### Calm Technology · Embedded Design · Robust by Architecture

A resilient Raspberry‑Pi‑based kiosk system with a focus on  
**calm user experience**, **embedded robustness**, and **clear system boundaries**.

---

## Motivation

This project started as a simple Raspberry Pi kiosk with a touchscreen.  
It evolved into an exploration of what makes a device trustworthy.

The goal is not feature richness, but **long‑term stability, clarity, and calm interaction**.

The system is designed to:
- reduce cognitive load
- explain itself quietly
- recover automatically from failure
- survive power loss and crashes
- behave like a device, not a script

---

## Design Principles

> Code is behavior.  
> Structure is responsibility.

- Security must not punish the user  
- Failure is expected and planned for  
- Calm technology over noisy feedback  
- Systems must recover, not complain  

A good device is calm in everyday use  
and merciless in failure recovery.

---

## Architecture Overview

The system is built in clearly separated layers:

Human (User / Perception)
└─ UI & UX (Tkinter)
└─ Python Application
└─ systemd (Linux Service Manager)
└─ Linux Kernel
└─ Hardware Watchdog (BCM2835)

Each layer observes and protects the one above it.  
No layer blindly trusts another.

---

## Features

### User Interface
- Fullscreen touch UI (Tkinter)
- Large touch targets
- Quote of the day
- Time & date
- Temperature & humidity
- Weather forecast
- Neopixel lighting (warm / cool / amber, dimmable)

### UX & Security
- PIN‑protected system menu
- Graceful PIN cooldown (no permanent lockout)
- Visual security feedback (icons & color instead of alerts)
- Calm countdown instead of error dialogs

### System Robustness
- Software watchdog (application level)
- Automatic restart via systemd
- Hardware watchdog (BCM2835)
- Clean shutdown with resource cleanup
- Read‑only root filesystem using OverlayFS

---

## Project Structure


kiosk/
├── main.py
├── config.py
├── setup_kiosk.sh
├── ui/
├── system/
├── sensors/
├── leds/
└── weather/

- `main.py` – orchestration only
- `ui/` – presentation and interaction
- `system/` – lifecycle, security, watchdogs
- domain modules are isolated and explicit

---

## Installation (Raspberry Pi)

1. Copy the project to:
/home/pi/kiosk

2. Run the setup script:
chmod +x setup_kiosk.sh ./setup_kiosk.sh

3. Enable the systemd hardware watchdog:
Edit `/etc/systemd/system.conf` and set:
RuntimeWatchdogSec=15
ShutdownWatchdogSec=10

Apply with:
sudo systemctl daemon-reexec

4. Enable read‑only root filesystem:
sudo raspi-config

→ Performance Options  
→ Overlay File System  
→ Root FS: Yes  
→ /boot FS: No  

5. Start the kiosk:
sudo systemctl start kiosk.service

The kiosk will start automatically on every reboot.

---

## Reliability & Recovery

| Failure | Recovery |
|------|----------|
| UI freeze | Software watchdog |
| App crash | systemd restart |
| Service hang | systemd watchdog |
| systemd hang | Hardware watchdog |
| Power loss | Read‑only root FS |

The system always returns to a known‑good state.

---

## Maintenance & Updates

To apply updates:
1. Disable OverlayFS
2. Reboot
3. Apply changes
4. Re‑enable OverlayFS
5. Reboot

All system changes are **explicit and reversible**.

---

## Calm Technology

This project follows the principles described by  
**Mark Weiser** and **John Seely Brown**.

Information moves from the center to the periphery.  
The system communicates state quietly and non‑intrusively.

A device should whisper, not shout.

---

## Intended Use

- Information kiosks
- Ambient displays
- Home automation panels
- Industrial HMI prototypes
- Embedded UX experiments
- Educational reference for embedded design

---

## Final Note

This project is less about what the system does  
and more about how it behaves when things go wrong.

**A good device is calm in everyday use  
and ruthless in recovery.**
































