#!/bin/sh

#This file will encrypt data inputted into it then move it to the send folder in which
# another script will send it off.

# mv "filename/path" "path destination"

python savetoCSV.py #savetoCSV.py shold be dataEncryption.py

echo Please Wait
sleep 5
bash sendFile.sh