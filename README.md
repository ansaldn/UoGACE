This section is for the networking for the UoGACE Project.

There are 5 main files to take into consideration.
dataCreation.py #Should come from the visual branch
savetoCSV.py - This file will take the data and return it to an external csv

sendFile.sh - this script takes the file and sends it a mulitple addresses (other raspberry pis, moonBuggy and both Bases) #To add, if successfull ping back message

encryptFile.sh - this file will encrypt the data (Or runs script for encryption program)
decryptFile.sh - This file will decrypt the data (Or runs script for decryption program)


Here you will find the following files that are to be used on certain devices in the network

moonBuggy:

On the Moon Buggy, you should have:
encryptData.sh - to encrypt data before sending
decryptData.sh - to decrypt data after receiving 
dataCreation - code used to add data to table

