#!/bin/sh

sudo cp /home/pi/Huskie-Vision/setup/VisionStartup.service  /etc/systemd/system/
sudo chmod u+rw  /etc/systemd/system/VisionStartup.service
sudo systemctl enable propanel
sudo systemctl daemon-reload
