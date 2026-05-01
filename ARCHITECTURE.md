# Architecture Overview
Raspberry Pi Kiosk System

This document explains the architectural decisions behind the kiosk system.
It focuses on *why* the system is structured the way it is, not on usage or installation.

The system is designed as a **device**, not as a script or demo application.


## Design Intent

The core intent of this system is **predictable behavior under real-world conditions**:

- power loss
- partial failure
- user error
- long unattended runtimes
- limited physical access

The architecture assumes that:
- failures are normal
- recovery must be automatic
- escalation must be layered
- the user must remain calm, not overwhelmed


## Architectural Principles

The system follows a small set of explicit principles:

- Code defines behavior
- Structure defines responsibility
- UX is part of system safety
- Failure is expected, not exceptional
- Every layer has an upper bound of trust


## Layered System Model

The system is intentionally built in layers:

Human (Perception)
UI / UX (Tkinter)
Application Logic (Python)
Service Management (systemd)
Operating System (Linux)
Hardware Watchdog (SoC)

Each layer is responsible for monitoring or protecting the layer above it.
No layer assumes that the next layer will always behave correctly.


## Responsibility by Layer

### Human / User

The human is considered part of the system.

Responsibilities:
- Interact via touch
- Understand visible system state
- Remain calm during temporary lockouts or delays

The system avoids alarming feedback.
Humans are not treated as adversaries.


### UI / UX Layer

Responsibilities:
- Present system state
- Reduce cognitive load
- Communicate security status visually
- Avoid modal overload and alerts

Non-responsibilities:
- No business logic
- No security decisions
- No lifecycle control

The UI is informational, not authoritative.


### Application Layer (Python)

Responsibilities:
- Coordinate domain modules
- Manage timing and state updates
- Perform graceful shutdown
- Self-monitor via software watchdog

Non-responsibilities:
- No hardware reset logic
- No OS-level recovery

The application knows when it can no longer be trusted
and exits explicitly when its own liveness is compromised.


### Service Layer (systemd)

Responsibilities:
- Start the application
- Restart on failure
- Enforce runtime expectations
- Escalate non-responsiveness

systemd is authoritative over the application lifecycle.
The application does not attempt to protect itself beyond its boundaries.


### Operating System Layer

Responsibilities:
- Resource management
- Process isolation
- Filesystem integrity
- Device drivers
- systemd supervision

The operating system is assumed to be mostly reliable,
but still subject to failure.


### Hardware Watchdog

Responsibilities:
- Ultimate system recovery
- Hardware-level reset when no other layer responds

The hardware watchdog is intentionally silent.
It exists as a last-resort safety mechanism.


## Watchdog Escalation Chain

The system uses a staged recovery model:

1. Software watchdog detects application unresponsiveness
2. Application terminates itself
3. systemd restarts the service
4. systemd runtime watchdog monitors system health
5. Hardware watchdog resets the system if needed

Each stage is stricter than the last.
Each stage assumes the previous one may fail.


## Filesystem Strategy

The root filesystem is treated as immutable during normal operation.

- Root filesystem: read-only (OverlayFS)
- Volatile data: RAM-backed tmpfs
- Application data: explicitly writable paths

This prevents:
- SD card corruption
- partial writes during power loss
- state drift over time

The system always boots into a known-good state.


## Security Model

Security is implemented as **behavior over time**, not as punishment.

- PIN protection uses delayed cooldowns
- No permanent lockouts
- No aggressive alarms
- Visual feedback replaces error messaging

Security mechanisms aim to reduce misuse
without triggering user panic or workarounds.


## Calm Technology

The system intentionally follows the principles of Calm Technology:

- State information moves to the periphery
- Color and symbols replace text where possible
- No unnecessary alerts or sounds
- The system communicates gently unless escalation is required

Calm UX is treated as a safety feature.


## What This Architecture Optimizes For

- Predictability
- Recoverability
- Longevity
- Understandability
- Minimal maintenance


## What This Architecture Does NOT Optimize For

- Feature density
- Maximum performance
- Competitive benchmarks
- Rapid UI experimentation

Those tradeoffs are intentional.


## Closing Statement

This architecture favors systems that:
- remain understandable under stress
- fail gently
- recover decisively

A device should never rely on everything going right.
It should be designed for what happens when things go wrong.
