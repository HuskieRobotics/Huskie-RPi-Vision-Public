#!/bin/sh


sudo sed -i 's/start_x=0/start_x=1/g' /boot/config.txt

sudo sed -i 's/gpu_mem=128/gpu_mem=256/g' /boot/config.txt

