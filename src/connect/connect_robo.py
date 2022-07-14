import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind(('localhost', 5000))
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    # data = conn.recv(4096).decode("UTF-8")
    # print(data)
    data = input("Введи сообщение: ")
    if not data:
        break
    conn.sendto(data.encode("UTF-8"),('localhost', 5000))

conn.close()
sock.close()