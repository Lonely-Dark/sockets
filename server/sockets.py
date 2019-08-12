#Python 3.7.3
#Make by Lonely-Dark

import socket 
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port=8080
s.bind(('localhost', port))
s.listen(2)
print("Server start!")
print("Initialization,wait")
time.sleep(1)
print("Waiting for connection")
while True:
	conn, addr = s.accept()
	data=conn.recv(1024)
	print("Connected: ", addr)
	print(data)
	conn.send(b'Text message')
	conn.close()
	time.sleep(0.1)

