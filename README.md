# arduino-python-energy-monitor
This project involves creating a Python-powered IoT-based energy monitoring and control system. The system will collect real-time data from connected sensors (e.g., power consumption, voltage, and current sensors) and provide a visual dashboard for analysis. Additionally, the system can control devices remotely, optimizing energy usage. 
# IoT Energy Monitoring System

This project monitors real-time energy usage using an Arduino and Python. The data is collected via a current sensor (ACS712) and visualized using Python.

## Features
- Real-time data acquisition using Arduino
- Dynamic visualization with Matplotlib
- Easy integration with energy-saving automation systems

## Hardware Requirements
- Arduino Uno
- ACS712 Current Sensor
- Jumper Wires

## Software Requirements
- Python 3.x
- Libraries: pyserial, matplotlib, pandas

## Installation
1. Upload the `energy_monitor.ino` sketch to the Arduino.
2. Connect the Arduino to your computer.
3. Run the Python script:
   ```bash
   python energy_monitor.py
