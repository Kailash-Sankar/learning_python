import socket

soc = socket.socket()  # create a socket object

soc.bind(('localhost', 12345))  # bind to a port

soc.listen(5)  # wait for the client connection

while True:
    # establish connection with client
    connection, address = soc.accept()
    print 'Got a client connection'
    greet = "hello from python training"

    connection.send(greet)
    connection.close()
