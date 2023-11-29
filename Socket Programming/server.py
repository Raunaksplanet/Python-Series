#!/usr/bin/python3

import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
ip = "127.0.0.1"
port = 8888



s.bind((ip,port))
print("Listening....") 
s.listen(1)
client,addr = s.accept()

print("Connected to the server\nIP: ",ip,"\nPort: ",port)
print("--------------------------")


while True:
	try:
		cmd = input("$ ")
		if cmd == "exit":
			break
		client.send(cmd.encode())
		output = (client.recv(1024)).decode()
		print(output)
	except Exception as e:
		print("Error Occured ", e)
		break



client.close()
s.close()
