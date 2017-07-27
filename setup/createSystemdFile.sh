#!/bin/sh

sudo cp /home/pi/RPi-Vision/Vision/VisionStartup.service  /etc/systemd/system/
sudo systemctl daemon-reload
