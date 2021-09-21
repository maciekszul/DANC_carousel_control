import socket
from psychopy import core


TCP_IP = "169.254.226.95"
TCP_PORT = 5005
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(buffer_size)
    if data.decode() == "connected":
        print("client connected")
        break

msg = "start"
conn.send(msg.encode())

timer = core.CountdownTimer(3)
while timer.getTime() > 0:
    msg = "record"
    conn.send(msg.encode())
msg = "stop"
conn.send(msg.encode())

while True:
    data = conn.recv(buffer_size)
    if "dump" in data.decode():
        print("dumped")
        break

conn.send("exit".encode())
s.close()