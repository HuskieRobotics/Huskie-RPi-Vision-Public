#!/bin/sh

#sudo apt-get update

#sudo apt-get upgrade
3read -rsp $'Press any key to continue...\n' -n1 key

sudo sh enableCamAdam.sh
#read -rsp $'Press any key to continue...\n' -n1 key

sudo sh pip_installs.sh
#read -rsp $'Press any key to continue...\n' -n1 key

sudo sh install-opencv3.2.sh

sudo sh createSystemdFile.sh

sudo apt-get reboot

