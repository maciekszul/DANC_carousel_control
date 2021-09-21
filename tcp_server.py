import socket

TCP_IP = "172.17.0.1"
TCP_PORT = 5005
buffer_size = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

print("CONNECTION ADDRESS:", addr)

while True:
    data = conn.recv(buffer_size)
    data_decoded = data.decode()
    if not data:
        break
    print("received:", data_decoded)
    conn.send(data)

conn.close()
