import socket
import time

TCP_IP = "169.254.226.95"
TCP_PORT = 5005
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

message_connect = "connected"
s.send(message_connect.encode())

time.sleep(1)

while True:
    data_raw = s.recv(buffer_size)
    data = data_raw.decode()
    if "start" in data:
        print(data)
        no, start = data.split("_")
        time.sleep(4)
        message_stop = no + "_stop"
        s.send(message_stop.encode())
        print(no, "recording stopped")
        time.sleep(2.5)
        message_dump = no + "_dumped"
        s.send(message_dump.encode())
        print(no, "data dumped")
    
    if "exit" in data:
        break

s.close()