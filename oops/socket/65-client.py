import socket

s = socket.socket()

port = 6341

ip = "192.168.1.129"

s.connect((ip,port))
print("connected to server")

s.send(b"Hello server , i am client")

s.close()

input()