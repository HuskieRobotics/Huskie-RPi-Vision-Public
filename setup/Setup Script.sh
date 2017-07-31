#!/bin/sh

sudo apt-get update
sudo apt-get upgrade
sh enable camera.sh
sh pip installs.sh
sh install-opencv3.2.sh
sh createSystemdFile.sh
sudo apt-get reboot

