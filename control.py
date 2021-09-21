import socket
import time


TCP_IP = "169.254.226.95"
TCP_PORT = 5005
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

print("CONNECTION ADDRESS:", addr)

# client connected
while True:
    data = conn.recv(buffer_size)
    if data.decode() == "connected":
        print("client connected")
        break

time.sleep(1)

for i in range(20):
    message_start = str(i).zfill(4) + "_start"
    conn.send(message_start.encode())
    print(message_start, "waiting for the stop")
    while True:
        data = conn.recv(buffer_size)
        if "stop" in data.decode():
            print(data.decode(), "recording stopped")
            break
    print("waiting for the dump")
    while True:
        data = conn.recv(buffer_size)
        if "dumped" in data.decode():
            print(data.decode(), "data dumped")
            break
conn.send("exit".encode())
conn.close()
