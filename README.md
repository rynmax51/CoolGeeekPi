# CoolGeeekPi

Fan control system for the Raspberry Pi 5 using GPIO PWM, designed specifically for the **GeeekPi PWM Fan** (dual 40mm 5V fans).

This project keeps your system cool under load and silent at idle.  
Tested and working on **Raspberry Pi OS Bookworm (64-bit)** and **Raspberry Pi 5**, with systemd support.

---

## 🚀 Features

- Automatically turns fans **on at 62°C** and **off below 49°C**
- Runs as a **systemd service**
- Uses **gpiozero** with `lgpio` backend (fully Pi 5 compatible)
- Simple `fanwatch` script for interactive debugging
- Clean install and uninstall scripts
- Live CPU temperature logging

---

## 🧰 Hardware

- **Fan model**: [GeeekPi PWM Fan (2-pack)](https://www.amazon.com/dp/B092YXQMX5)
- Power: 5V
- Control: Dual GPIO PWM (GPIO18 and GPIO13)

### 🔌 Wiring Guide

| Wire Color | Connects To              |
|------------|--------------------------|
| Red        | 5V (Pin 2 or 4)          |
| Black      | GND (Pin 6 or 9)         |
| Blue       | GPIO18 / GPIO13 (Pins 12 & 33) |

> Top fan = GPIO18  
> Bottom fan = GPIO13

---

## 🛠️ Installation

```bash
git clone https://github.com/rynmax51/CoolGeeekPi.git
cd CoolGeeekPi
sudo ./install.sh
```

### To uninstall:

```bash
sudo ./uninstall.sh
```

---

## 🔍 How It Works

- Monitors CPU temperature via `/sys/class/thermal/thermal_zone0/temp`
- Turns both fans on at full speed when temp ≥ 62°C
- Turns them off again when temp ≤ 49°C
- Status is printed every 5 seconds
- Automatically starts on boot via systemd

---

## 🧪 Testing (fanwatch)

Use this to temporarily stop the background service and run interactively:

```bash
fanwatch
```

You'll see live readouts like:

```
Temp: 58.4°C | Fans: OFF
Temp: 63.2°C | Fans: ON
Temp: 59.9°C | Fans: ON
Temp: 47.6°C | Fans: OFF
```

---

## ⚙️ systemd Notes

This service runs as user `pi`.

On Raspberry Pi OS Bookworm, the default systemd environment is too limited for `lgpio`.  
So the service is configured to use:

```ini
WorkingDirectory=/home/pi
```

This workaround is required to let the `lgpio` backend create `.lgd-nfyX` notification pipes.

---

## 📁 File Structure

```
CoolGeeekPi/
├── install.sh
├── uninstall.sh
├── opt/
│   └── coolgeeekpi/
│       ├── fan_control.py
│       └── fanwatch
└── etc/
    └── systemd/
        └── system/
            └── coolgeeekpi.service
```

---

## 🙌 Author

**[@rynmax51](https://github.com/rynmax51)**  
Created to simplify repeatable setup and deployment of fan control on modern Raspberry Pi systems.
