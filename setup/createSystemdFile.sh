#!/bin/sh

sudo cp /home/pi/Huskie-Vision/setup/VisionStartup.service  /etc/systemd/system/
sudo chmod 777 /etc/systemd/system/VisionStartup.service
sudo systemctl daemon-reload
