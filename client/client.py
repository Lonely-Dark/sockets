#Python 3.7.3
#Make by Lonely-Dark

import socket
sock=socket.socket()
sock.connect(('localhost', 8080))
sock.send('Hello world!')
data=sock.recv(1024)
sock.close()
print(data)
