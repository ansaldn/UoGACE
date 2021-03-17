#!/bin/sh

scp /Users/davidansa/Projects/sendFile/send.txt pi@192.168.1.112:sendFolder #PATH MUST CHANGE FROM PI TO ANOTHER PI
sendFile.sh
scp /Users/davidansa/UoGACE/Network/LAN/data.csv pi@192.168.1.112:receiveFolder #Same as above
echo Successfully Sent!
