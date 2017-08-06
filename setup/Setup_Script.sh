#!/bin/sh

sudo apt-get update
sudo apt-get upgrade
sh enable_camera.sh
sh pip_installs.sh
sh install-opencv3.2.sh
sh createSystemdFile.sh
sudo apt-get reboot

