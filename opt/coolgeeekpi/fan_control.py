#!/usr/bin/env python3

from gpiozero import PWMOutputDevice
from time import sleep

# =============================
# CoolGeeekPi Fan Control Logic
# =============================

# --- CONFIGURATION ---
FAN_ON_TEMP = 62    # (°C) Turn fans ON at or above this temperature
FAN_OFF_TEMP = 49   # (°C) Turn fans OFF below this temperature

# GPIO pin assignments
TOP_FAN_GPIO = 18      # GPIO18 (Physical Pin 12)
BOTTOM_FAN_GPIO = 13   # GPIO13 (Physical Pin 33)

# --- FAN SETUP ---
top_fan = PWMOutputDevice(TOP_FAN_GPIO)
bottom_fan = PWMOutputDevice(BOTTOM_FAN_GPIO)
fan_is_on = False  # Internal state tracker

# --- TEMP SENSOR ---
def get_cpu_temp():
    """Read the CPU temperature from thermal_zone0."""
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        return int(f.read()) / 1000.0

# --- MAIN LOOP ---
try:
    print("CoolGeeekPi fan control running. Press Ctrl+C to exit.")
    while True:
        temp = get_cpu_temp()

        if not fan_is_on and temp >= FAN_ON_TEMP:
            top_fan.value = 1.0
            bottom_fan.value = 1.0
            fan_is_on = True
            print(f"Temp: {temp:.1f}°C | Fans: ON")

        elif fan_is_on and temp <= FAN_OFF_TEMP:
            top_fan.value = 0.0
            bottom_fan.value = 0.0
            fan_is_on = False
            print(f"Temp: {temp:.1f}°C | Fans: OFF")

        else:
            print(f"Temp: {temp:.1f}°C | Fans: {'ON' if fan_is_on else 'OFF'}")

        sleep(5)

except KeyboardInterrupt:
    print("Exiting fan control...")

finally:
    # Always turn off fans on exit
    top_fan.value = 0.0
    bottom_fan.value = 0.0
    print("Fans stopped.")
