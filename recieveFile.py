import socket
import os

file = open("test.py", "wb")
sock = socket.socket
sock.connect("192.168.1.7", 5001)

file.close()
print("Data Recieved")
