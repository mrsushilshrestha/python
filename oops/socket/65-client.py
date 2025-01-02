import socket

s = socket.socket()

port = 1234

ip = "127.0.0.1"

s.connect((ip,port))
print("connected to server")

s.send(b"Hello server , i am client")

s.close()

input()