---
layout: default
title: GUI User Guide
---

# GUI User Guide

[Back to Home](./)

---

## GUI Layout

The interface is organized top to bottom:

| Row | Section | Purpose |
|-----|---------|---------|
| 0 | Pump Image | Visual reference of the pump hardware |
| 1 | Multi Pump Connect | Connect multiple pumps by entering serial numbers |
| 2 | Connect / Serial | Auto-connect or manually enter a serial / device path |
| 3 | Flowrate Quick Adjust | Type a number (0-40) to change flow rate on the fly |
| 4 | On/Off + Direction | Turn the pump on/off and toggle flow direction |
| 5 | Flow Behavior | Select a flow mode, enter parameters, and apply |
| 6 | Pause / Resume / Restart | Control scheduled command execution |
| 7 | File Buttons | Create experiment, upload/change/run/exit text files |
| 8 | File Labels | Shows the currently selected file name |
| 9 | File Contents Display | Human-readable preview of loaded commands |

---

## Connecting Pumps

### Auto Connect

Click **Auto Connect**. The software scans USB ports and connects to the first likely Arduino device. The button turns green on success.

### Manual Connect

Type a USB serial number (e.g., `054433A493735191B7D8`) or a device path (e.g., `/dev/cu.usbmodem1101`) into the serial input field and press Enter.

### Multiple Pumps

1. Enter the number of pumps (1-10) in the "Connect multiple pumps" field and press Enter.
2. A popup appears - enter the serial number for each pump.
3. Click **Collect Serial #s**. The software connects to each Arduino.
4. Use the dropdown to switch between connected pumps.

---

## Pump Controls

### On/Off

- Click **Pump: OFF** to turn the pump on (sends `123` to Arduino).
- Click **Pump: ON** to turn it off (sends `0` to Arduino).
- Button color: green = on, red = off.

### Direction

- Click **Direction** to toggle between forward (`-->`) and backward (`<--`).
- Sends `321` to the Arduino.
- Only works when the pump is on.

### Quick Flowrate Adjust

Type an integer (0-40) in the flowrate field and press Enter. Sends the number directly to the Arduino, which recalculates the servo delay for that flow rate in uL/min.

---

[Next: Flow Behaviors](flow.html) | [Back to Home](./)
