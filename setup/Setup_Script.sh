#!/bin/sh

#sudo apt-get -y update

#sudo apt-get -y upgrade


sudo sh /home/pi/Huskie-RPi-Vision-Public/setup/enableCamAdam.sh


sudo sh /home/pi/Huskie-RPi-Vision-Public/setup/pip_installs.sh


sudo sh /home/pi/Huskie-RPi-Vision-Public/setup/install-opencv3.2.sh
cd /home/pi/Huskie-RPi-Vision-Public/setup/

sudo sh /home/pi/Huskie-RPi-Vision-Public/setup/createSystemdFile.sh

#sudo shutdown -r now
