#!/usr/bin/env python3
"""Launch the pump GUI from the repo root (works with `uv run python run_gui.py`)."""
import os
import runpy
import sys

gui_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Python code")
os.chdir(gui_dir)
sys.path.insert(0, gui_dir)
runpy.run_path("GUI.py", run_name="__main__")
