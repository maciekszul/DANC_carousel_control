import socket

TCP_IP = "172.17.0.1"
TCP_PORT = 5005
buffer_size = 1024

message = bytearray("hello world".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(message)
data = s.recv(buffer_size)

s.close()

print("received:", data)