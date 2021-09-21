import socket

TCP_IP = "169.254.226.95"
TCP_PORT = 5005
buffer_size = 20

message = bytearray("hello world".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    value = input("Type a message:")
    if value == "exit":
        break
    s.send(value.encode())
    data = s.recv(buffer_size)
    
s.close()