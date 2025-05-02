#!/bin/bash
set -e

echo "Uninstalling CoolGeeekPi..."

# Stop and remove service
sudo systemctl stop coolgeeekpi.service || true
sudo systemctl disable coolgeeekpi.service || true
sudo rm -f /etc/systemd/system/coolgeeekpi.service
sudo systemctl daemon-reload

# Remove files
echo "Removing /opt/coolgeeekpi..."
sudo rm -rf /opt/coolgeeekpi

echo "Removing fanwatch global command..."
sudo rm -f /usr/local/bin/fanwatch

# Clear shell command cache
hash -r 2>/dev/null || true

echo "✅ CoolGeeekPi fully uninstalled."
