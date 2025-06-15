#!/bin/sh

# Start Xvfb
Xvfb :99 -screen 0 1024x768x24 &
export DISPLAY=:99

# Start the application
python resume_parser.py
