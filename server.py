import socket

TCP_IP = "169.254.226.95"
TCP_PORT = 5005
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

print("CONNECTION ADDRESS:", addr)

while True:
    data = conn.recv(buffer_size)
    try:
        data_decoded = data.decode()
        if data:
            print(data_decoded)
        value = input("Type a message:")
        if value == "exit":
            break
        conn.send(value.encode())
    except KeyboardInterrupt:
        conn.close()
