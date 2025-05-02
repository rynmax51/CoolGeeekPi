#!/bin/bash
set -e

echo "Installing CoolGeeekPi..."

# Install dependencies
echo "Installing gpiozero (if needed)..."
sudo apt-get update
sudo apt-get install -y python3-gpiozero

# Copy files
echo "Copying files to /opt/coolgeeekpi..."
sudo mkdir -p /opt/coolgeeekpi
sudo cp opt/coolgeeekpi/fan_control.py /opt/coolgeeekpi/
sudo cp opt/coolgeeekpi/fanwatch /opt/coolgeeekpi/
sudo chmod +x /opt/coolgeeekpi/fanwatch

# Link fanwatch globally
echo "Linking fanwatch command..."
sudo ln -sf /opt/coolgeeekpi/fanwatch /usr/local/bin/fanwatch

# Install systemd service
echo "Installing systemd service..."
sudo cp service/coolgeeekpi.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable coolgeeekpi.service
sudo systemctl start coolgeeekpi.service

echo "✅ CoolGeeekPi installed and running."
