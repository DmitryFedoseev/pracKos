import socket

#IP = "127.0.0.1"
sock = socket.socket()
sock.connect(('localhost', 5000))
while True:
    sock.send(input().encode("UTF-8"))

    data = sock.recv(1024)

sock.close()
