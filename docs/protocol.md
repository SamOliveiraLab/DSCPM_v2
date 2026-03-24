---
layout: default
title: Arduino Protocol
---

# Arduino Command Protocol

[Back to Home](./)

---

Communication runs at **9600 baud**. The Arduino sends `READY` on startup; Python waits for this before proceeding.

## Commands (Python to Arduino)

| Command | Action |
|---------|--------|
| `0` | Turn pump off. Saves position to EEPROM. |
| `123` | Turn pump on. |
| `321` | Toggle flow direction. |
| `456` | Request status log (position, direction, valve state). |
| Any float (e.g., `10.5`) | Set flow rate in uL/min. Recalculates servo delay. |
| `FLOWA,{rate}` | Constant flow mode *(firmware update required)*. |
| `FLOWB,{rate},{duty},{freq}` | Pulse mode *(firmware update required)*. |
| `FLOWC,{rate},{freq},{amp}` | Oscillation mode *(firmware update required)*. |
| `FLOWD,{rate},{pfreq},{duty},{oamp},{ofreq}` | Pulse of Oscillation mode *(firmware update required)*. |

## Responses (Arduino to Python)

| Response | When |
|----------|------|
| `READY` | On startup, signals handshake complete |
| `System OFF. Position saved.` | After command `0` |
| `Pumps ON` | After command `123` |
| `Direction switched.` | After command `321` |
| `LOG: Position: X, FWD: Y...` | After command `456` |
| `Flow rate changed to X uL/min` | After a numeric flow rate command |

## Hardware Pinout

| Pin | Function |
|-----|----------|
| 9 | Servo motor 1 |
| 11 | Servo motor 2 |
| 5 | Solenoid valve 1 |
| 6 | Solenoid valve 2 |
| 10 | Solenoid valve 3 |

## Syringe Parameters (in firmware)

| Parameter | Value |
|-----------|-------|
| Inner diameter | 0.485 mm |
| mm per degree | 0.256 |
| Default flow rate | 1.5 uL/min |
| Servo range | 5 - 70 degrees |

---

[Back to Home](./)
