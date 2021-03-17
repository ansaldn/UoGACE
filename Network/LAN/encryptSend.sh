#!/bin/sh

#This file will encrypt data inputted into it then move it to the send folder in which
# another script will send it off.

# mv "filename/path" "path destination"

python saveSecure.py #This codes saves the input from another node i.e. moonBuggy and encrypts data before uploading to csv

echo Please Wait
sleep 5
bash sendFile.sh
