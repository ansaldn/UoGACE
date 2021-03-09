#!/bin/sh

scp /Users/davidansa/Projects/sendFile/send.txt pi@192.168.1.112:sendFolder #PATH MUST CHANGE FROM PI TO ANOTHER PI
scp /Users/davidansa/UoGACE/data.csv pi@192.168.1.112:receiveFolder #Same as above
echo Successfully Sent!
