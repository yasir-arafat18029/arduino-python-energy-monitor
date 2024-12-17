import serial
import time
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

# Serial Port Configuration
SERIAL_PORT = 'COM3'  # Replace with your port (e.g., '/dev/ttyUSB0' on Linux)
BAUD_RATE = 9600

# Data Storage
current_values = deque(maxlen=50)  # To store the last 50 current values
timestamps = deque(maxlen=50)

# Initialize Serial Connection
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print("Connected to Arduino on", SERIAL_PORT)
except Exception as e:
    print(f"Error: {e}")
    exit()


# Function to Update Plot
def update_plot():
    plt.cla()
    plt.plot(timestamps, current_values, color='b', label='Current (A)')
    plt.xlabel('Time')
    plt.ylabel('Current (A)')
    plt.title('Real-Time Energy Monitoring')
    plt.legend()
    plt.grid()


# Data Acquisition and Visualization Loop
try:
    print("Reading data... Press Ctrl+C to stop.")
    plt.ion()  # Turn on interactive mode for Matplotlib
    fig = plt.figure()

    while True:
        # Read data from Arduino
        if arduino.in_waiting > 0:
            raw_data = arduino.readline().decode('utf-8').strip()
            try:
                current = float(raw_data)
                current_values.append(current)
                timestamps.append(time.strftime('%H:%M:%S'))
                print(f"Current: {current:.2f} A")

                # Update the plot
                update_plot()
                plt.pause(0.1)

            except ValueError:
                print("Invalid data received, skipping...")

except KeyboardInterrupt:
    print("Program stopped by user.")
    arduino.close()
    print("Serial connection closed.")
