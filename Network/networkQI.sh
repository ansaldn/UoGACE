#!/bin/sh

: ' For the quickest installation of anything used within this branch, run this script by saving this file to an 
internet connect Pi and entering ./networkQI.sh into the terminal window. '

sudo apt-get install python #If python is already installed nothing will happen
sleep 5
python -m pip install cryptography
echo Installed Successfully