# Notes on Failure and Recovery
Raspberry Pi Kiosk System

This document describes situations that may appear like failures,
but are normal or intentional behaviors of the system.

It also clarifies when a situation is truly abnormal
and requires human intervention.


## Design Assumption

This system assumes that:
- failures will happen
- power may be lost at any time
- software may temporarily hang
- users may make mistakes

Failure is not treated as an exception,
but as an expected operating condition.


## Situations That May Look Like Failures (But Are Normal)

### Temporary UI Unresponsiveness

What you may observe:
- Touch input does not respond
- Elements stop updating briefly

What is happening:
- Internal monitoring may detect instability
- The application may be preparing to restart

Recommended action:
- Wait and observe
- Do not force input
- Do not power-cycle immediately


### Automatic Application Restart

What you may observe:
- Screen briefly turns black
- UI reappears without user interaction

What is happening:
- The software watchdog or systemd restarted the application
- This is a protective action

Recommended action:
- No action needed
- Normal operation resumes automatically


### Automatic System Reboot

What you may observe:
- The device reboots without warning
- Startup screen briefly appears

What is happening:
- A severe fault was detected
- The hardware watchdog reset the system
- This is intentional and protective

Recommended action:
- Allow the reboot to complete
- The system should return to normal operation


### PIN Access Temporarily Locked

What you may observe:
- System menu cannot be opened
- Lock symbol appears
- Countdown is shown

What is happening:
- Too many incorrect PIN attempts
- Temporary cooldown is active

Recommended action:
- Wait until the countdown finishes
- No reset or power cycle is required


### Loss of Configuration Changes After Reboot

What you may observe:
- Manual system changes disappear after reboot

What is happening:
- Read-only root filesystem with OverlayFS
- Runtime changes are intentionally discarded

Recommended action:
- Use maintenance mode for permanent changes


## Situations That Are Abnormal

### No Display Output After Several Minutes

Possible causes:
- Display or cable issue
- Power supply problem
- Hardware fault

Recommended action:
- Check power
- Check display connection
- Inspect hardware


### Device Does Not Power On

Possible causes:
- Power adapter failure
- Cable damage
- Board failure

Recommended action:
- Verify power source
- Try known-good power supply


### Continuous Reboot Loop

Possible causes:
- Corrupted SD card
- Incompatible update
- Hardware instability

Recommended action:
- Power off the device
- Inspect logs (if available)
- Reflash SD card if necessary


## What the System Will Never Do Silently

The system will not:
- Permanently lock itself without recovery
- Destroy stored application code
- Require frequent manual resets
- Accumulate hidden state over time

If such behavior is observed, it indicates a genuine fault.


## Philosophy of Failure Handling

The system follows a layered recovery approach:
- Minor problems are corrected locally
- Larger problems trigger escalation
- Unrecoverable states lead to reset

This approach minimizes user involvement
and maximizes predictability.


## Final Guidance

If something looks wrong:
- Pause
- Observe
- Allow the system to react

In most cases, no intervention is needed.

The system is designed to recover quietly and decisively.
