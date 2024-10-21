#!/bin/bash

# Enable UFW
echo "Enabling UFW..."
sudo ufw enable

# Allow common ports
echo "Allowing HTTP (port 80) and HTTPS (port 443)..."
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Block FTP
echo "Blocking FTP (port 21)..."
sudo ufw deny 21/tcp

# Display UFW status
echo "Current firewall status:"
sudo ufw status verbose
