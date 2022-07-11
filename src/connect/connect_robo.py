import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5001))
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(4096).decode("UTF-8")
    if not data:
        break
    print(data)

conn.close()