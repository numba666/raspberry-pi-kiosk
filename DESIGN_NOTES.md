# Design Notes
Raspberry Pi Kiosk System

These notes capture architectural and design insights gained while building
this system. They are intentionally reflective and principle-oriented.

This document is not about implementation details.
It is about transferable thinking.


## From Project to Device

The most important shift during this project was the realization that
a kiosk is not an application, but a device.

An application is launched.
A device exists.

This distinction changes how responsibility is assigned:
- A device must recover on its own
- A device must explain its state
- A device must tolerate misuse and failure
- A device must survive power loss


## Code vs. Structure

One central realization:

Code defines behavior.  
Structure defines responsibility.

Many failures are not caused by incorrect code,
but by unclear structural boundaries.

Explicit boundaries reduce:
- accidental coupling
- hidden assumptions
- panic-driven fixes


## Failure as a First-Class Concept

Failure was not treated as an edge case, but as a design input.

Instead of asking:
"What if this fails?"

The design asked:
"When this fails, what should happen?"

This led to:
- layered watchdogs
- explicit escalation paths
- calm user feedback
- automatic recovery without human intervention


## UX Is Part of Safety

User experience was treated as part of system safety,
not as a cosmetic layer.

Security mechanisms that punish or surprise users
lead to workarounds and mistrust.

The system favors:
- proportional response
- temporary cooldowns
- visual feedback
- waiting over blocking

Calm behavior reduces error rates.


## Calm Technology in Practice

The concept of Calm Technology was not used as an aesthetic principle,
but as a safety tool.

Information is present,
but it moves to the periphery until needed.

Color, symbols, and timing replace alerts and dialogs.

A calm system is less likely to be disrupted by impulsive interaction.


## Time as an Organizing Principle

Another key insight:
Time is a design tool.

Cooldowns, delays, watchdog intervals,
and recovery timing shape system behavior
as much as structure does.

Time allows:
- emotions to settle
- systems to stabilize
- complexity to remain manageable


## Layered Trust Model

No layer is fully trusted.

- UI does not trust application state
- Application does not trust itself indefinitely
- systemd does not trust services
- Kernel does not trust userspace
- Hardware watchdog trusts no one

Each layer is responsible for the one above it.


## Read-Only Systems and Longevity

Mutable systems drift over time.

By assuming immutability during normal operation,
the system avoids:
- configuration drift
- partial updates
- silent corruption
- accumulated error

A reboot restores clarity.


## What Would Be Done Differently Next Time

Now that the structure is clear, a future iteration could:
- externalize configuration more cleanly
- abstract UI state from domain logic earlier
- design update workflows from the start

These are evolution points, not regrets.


## Transferable Lessons

The following principles apply beyond this project:

- Design for recovery, not perfection
- Use escalation, not exception handling
- Let systems explain themselves
- Treat the human as part of the system
- Favor calm, predictable behavior
- Make failure boring


## Closing Thought

A well-designed system does not strive to avoid failure.
It strives to make failure unremarkable.

Calm systems build trust.
