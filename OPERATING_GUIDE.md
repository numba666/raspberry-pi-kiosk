# Operating Guide
Raspberry Pi Kiosk System

This document describes how to operate and maintain the kiosk system in daily use.
It is written for operators and users, not for developers.


## Normal Operation

Under normal conditions, the system requires no interaction beyond the touchscreen.

Expected behavior:
- The device starts automatically after power-on
- The kiosk UI appears without login
- All information updates automatically
- The system can run unattended for long periods

No regular maintenance is required during normal operation.


## Using the System Menu

The system menu is opened via the ⚙ icon.

To access it:
- Press the ⚙ icon
- Enter the PIN when prompted

Available actions:
- Exit kiosk mode
- Reboot the device
- Shut down the device

The system menu is protected against accidental access.


## PIN Protection Behavior

The PIN system is designed to prevent misuse without frustrating the user.

- After several incorrect PIN attempts, access is temporarily locked
- A calm countdown indicates when access is available again
- No permanent lockout occurs
- No reboot is required

During the cooldown period, simply wait until access is restored.


## Visual System Feedback

The system communicates its state visually:

- ⚙ icon (normal color): system ready
- 🔒 icon (muted color): temporary security cooldown active
- Countdown: remaining cooldown time

No alarms or alerts are used.
The system is designed to remain calm and understandable.


## What To Do If The UI Appears Frozen

If the UI does not react to touches:

- Do nothing
- Wait briefly

The system includes internal monitoring that will automatically restart
the application if necessary.

In rare cases, the system may reboot itself.
This behavior is intentional.


## Power Loss and Reboot Behavior

Power loss is considered a normal operating condition.

Expected behavior:
- The system may lose power at any time
- No data corruption occurs
- On power return, the system starts automatically
- The previous state is restored

No user action is required after power loss.


## System Updates and Maintenance

Updates are performed intentionally and explicitly.

For maintenance:
- Temporarily disable read-only mode
- Reboot
- Apply updates or changes
- Re-enable read-only mode
- Reboot again

This procedure prevents accidental system changes
and ensures stability.


## What Not To Do

- Do not force power cycles repeatedly
- Do not try to modify system files during normal operation
- Do not disable protection mechanisms unless performing maintenance
- Do not expect the system to store long-term state during runtime

The system is designed to reset safely and regularly.


## Expected Self-Protection Behavior

The system may:
- Restart the application automatically
- Reboot itself in case of serious failure

These actions are protective, not errors.


## When To Intervene Manually

Manual intervention is only required if:
- The device does not power on
- The device does not display anything after several minutes
- Physical damage is suspected

In all other cases, allow the system to recover on its own.


## Design Philosophy For Operators

This device is designed to be:
- Calm
- Predictable
- Self-healing
- Transparent in behavior

If the device appears to pause or restart,
it is usually doing so deliberately to protect itself.


## Final Reminder

The safest action in most situations is:
**Wait and observe.**

The system is built to take care of itself.
