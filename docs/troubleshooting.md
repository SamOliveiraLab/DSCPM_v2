---
layout: default
title: Troubleshooting
---

# Troubleshooting

[Back to Home](./)

---

### App won't start / ModuleNotFoundError

- Install dependencies: `pip install PyQt5 pyserial`
- Run from inside the `Python code/` directory so relative imports work.

---

### "No device found" on connect

- Check that the Arduino is plugged in via USB.
- On macOS, verify the device appears: `ls /dev/cu.*`
- Try entering the device path manually (e.g., `/dev/cu.usbmodem1101`).

---

### Connect button turns red

The auto-detection couldn't find a matching device. Try manual serial entry or check the USB cable.

---

### Pump doesn't respond to FLOW commands

The Arduino firmware (`pump_JS_07222025.ino`) does not yet handle `FLOWA`/`FLOWB`/`FLOWC`/`FLOWD` commands. Numeric flow rate changes and on/off/direction work. The firmware needs an update to parse the new comma-separated flow commands.

---

### Pause/Resume not working

These buttons only work when a text file schedule is running. For manual control, use the On/Off button directly.

---

### File displays "no valid commands found"

Check that the file uses the correct format:

```
SERIAL*********COMMAND#########DELAY
```

with `%%%%%%%%%` between entries.

---

### Multiple pumps - wrong pump receives commands

- Use the pump dropdown to select which pump you're controlling manually.
- In text files, make sure each command uses the correct serial number for the target pump.

---

### macOS "app is damaged" warning

If macOS blocks `PumpGUI.app`, run this in terminal:

```bash
xattr -cr dist/PumpGUI.app
```

Then try opening it again.

---

[Back to Home](./)
