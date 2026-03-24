---
layout: default
title: Experiment Builder
---

# Experiment Builder

[Back to Home](./)

---

## Pause / Resume / Restart

These buttons control scheduled command execution:

| Button | Action |
|--------|--------|
| **Pause** | Sends `0` to stop the pump. Freezes the scheduler. Remaining command times are shifted so timing is preserved on resume. |
| **Resume** | Sends `123` to restart the pump. Continues from where it paused. |
| **Restart Cycle** | Stops execution, recalculates all times from original delays, and reruns the full sequence. |

---

## Running Text Files

### Upload a File

Click **Upload .txt file**, browse to your file, and select it. The contents appear in the preview area at the bottom.

### Run a File

Click **Run .txt file**. Commands execute on a background thread at the scheduled times.

- If a worker is already running, new commands merge into the existing schedule.
- If a serial number doesn't match but only one board is connected, it falls back to that board.

### Change File

Click **Change current file** to cycle through previously uploaded files.

### Stop Execution

Click **Exit current file** to kill the scheduler, stop the pump, and clear all commands.

---

## Create Experiment Dialog

Click the purple **Create Experiment** button to build command sequences visually.

### Adding Steps

1. **Select a pump** from the dropdown.
2. **Enter the time** in seconds from the start.
3. **Choose a behavior:** Turn On, Turn Off, Change Direction, Constant, Pulse, Oscillation, or Pulse of Oscillation.
4. **Fill in the parameters** that appear.
5. Click **Add Step**. It appears in the table.
6. Repeat for all steps.

### Managing Steps

- Select a row and click **Remove Selected** to delete it.
- Steps are sorted by time when the file is generated.

### Generating the File

Click **Generate & Save File**. Choose a save location. The software:

1. Writes the `.txt` file to disk.
2. Loads it as the current file in the main GUI.
3. Displays the parsed commands in the preview.

Then click **Run .txt file** to execute.

### Example Sequence

| Step | Time | Action |
|------|------|--------|
| 1 | 0 s | Turn On |
| 2 | 2 s | Constant flow at 10 uL/min |
| 3 | 30 s | Switch to Pulse (15 uL/min, 50% duty, 2 Hz) |
| 4 | 60 s | Turn Off |

---

## Text File Format

Command files use entries separated by `%%%%%%%%%`:

```
SERIAL*********COMMAND#########DELAY%%%%%%%%%SERIAL*********COMMAND#########DELAY
```

| Field | Description |
|-------|-------------|
| `SERIAL` | Arduino USB serial number (e.g., `054433A493735191B7D8`) |
| `COMMAND` | Any valid command string |
| `DELAY` | Time in seconds from start of execution |

### Example File

```
054433A493735191B7D8*********123#########0%%%%%%%%%054433A493735191B7D8*********FLOWA,10.0#########2%%%%%%%%%054433A493735191B7D8*********FLOWB,15.0,0.5,2.0#########30%%%%%%%%%054433A493735191B7D8*********0#########60
```

---

[Back to Home](./)
