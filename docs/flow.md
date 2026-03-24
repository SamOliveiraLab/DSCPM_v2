---
layout: default
title: Flow Behaviors
---

# Flow Behaviors

[Back to Home](./)

---

Select a mode from the **Flow Behavior** dropdown, fill in the visible parameters, then click **Apply Flow** to send the command to the Arduino.

## Constant

Steady flow in one direction.

| Parameter | Description |
|-----------|-------------|
| Flow Rate (uL/min) | 0 - 40 |

**Command sent:** `FLOWA,{rate}`

---

## Pulse

Intermittent on/off bursts.

| Parameter | Description |
|-----------|-------------|
| Flow Rate (uL/min) | 0 - 40 |
| Duty Cycle (0-1) | Fraction of each cycle the pump is active |
| Pulse Freq (Hz) | Number of cycles per second |

**Command sent:** `FLOWB,{rate},{duty},{freq}`

---

## Oscillation

Back-and-forth flow.

| Parameter | Description |
|-----------|-------------|
| Flow Rate (uL/min) | 0 - 40 |
| Osc Freq (Hz) | Oscillation frequency |
| Osc Amplitude | Amplitude of the oscillation |

**Command sent:** `FLOWC,{rate},{freq},{amplitude}`

---

## Pulse of Oscillation

Pulsed bursts of oscillatory flow — combines both behaviors.

| Parameter | Description |
|-----------|-------------|
| Flow Rate (uL/min) | 0 - 40 |
| Pulse Freq (Hz) | Frequency of the pulse envelope |
| Duty Cycle (0-1) | Fraction of each pulse cycle that is active |
| Osc Amplitude | Amplitude of oscillation within each pulse |
| Osc Freq (Hz) | Frequency of oscillation within each pulse |

**Command sent:** `FLOWD,{rate},{pulse_freq},{duty},{osc_amplitude},{osc_freq}`

---

> **Note:** The Arduino firmware must be updated to parse and execute the `FLOW` commands. The current firmware only handles constant flow via numeric flow rate values.

---

[Back to Home](./)
