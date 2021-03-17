# Network Introduction
This section is for the networking for the UoGACE Project. It covers all the communcation that occurs between different raspberry pis (nodes, bases). To begin with,

## Quick Installation Guide

If you have not already clone this repo. This can be done with this command in the terminal

```bash
git clone https://github.com/da5905p/UoGACE.git
```
*Please Note: GitHub must be previously installed, if it has not been follow the Quick Install Guide on the (Wiki)[https:github.com/da5905p/UoGACE/wiki]*

## Order of Use

There are 5 main files to take into consideration.
dataCreation.py #Should come from the visual branch
saveSecure.py - This file will take the data, encrypt it and return it to an external csv

sendFile.sh - this script takes the file and sends it a multiple addresses (other raspberry pis, moonBuggy and both Bases)  
encryptSend.sh - this file will encrypt the data and proceed to run the script that will send it to other nodes. 
decryptFile.sh - This file will decrypt the data and run the script that will read the data for use elsehwere.

## Device Requirements
Here you will find the following files that are to be used on certain devices in the network. Note: _Not all nodes need all files for it to work_

router:
encryptData.sh - to encrypt data before sending
decryptData.sh - to decrypt data after receiving
dataCreation - code used to add data to table
data.csv - This is the file that holds all of the encrypted data. All data is decrypted at the nodes for best security

moonBuggy:
On the Moon Buggy, you should have:
encryptData.sh - to encrypt data before sending
decryptData.sh - to decrypt data after receiving
dataCreation - code used to add data to table

Base (1&2)
encryptData.sh - to encrypt data before sending
decryptData.sh - to decrypt data after receiving
dataCreation - code used to add data to table
