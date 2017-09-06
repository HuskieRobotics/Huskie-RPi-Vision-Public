#!/bin/sh

sudo apt-get -y update

sudo apt-get -y upgrade

sudo sh /home/pi/Huskie-Vision/setup/enableCamAdam.sh

sudo sh /home/pi/Huskie-Vision/setup/pip_installs.sh

sudo sh /home/pi/Huskie-Vision/setup/install-opencv3.2.sh
cd /home/pi/Huskie-Vision/setup/

sudo sh /home/pi/Huskie-Vision/setup/createSystemdFile.sh

sudo shutdown -r now
