#!/bin/sh

scp /Users/davidansa/Projects/sendFile/send.txt pi@192.168.1.112:sendFolder -y et1mob1m #PATH MUST CHANGE FROM PI TO ANOTHER PI
sendFile.sh
expect 'Password'
send 'et1mob1m'
scp /Users/davidansa/UoGACE/Network/LAN/data.csv pi@192.168.1.112:receiveFolder #Same as above
echo Successfully Sent!
