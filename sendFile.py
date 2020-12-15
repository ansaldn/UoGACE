import socket

file = open("test.py". "rb")
sock = socket.socket()
sock.connect(("192.168.1.7", 5001)) 
