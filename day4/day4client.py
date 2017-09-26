import socket

soc = socket.socket()
soc.connect(('localhost',12345))
msg = soc.recv(1024)
print msg
