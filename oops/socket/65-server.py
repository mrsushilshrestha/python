import socket

s= socket.socket()

port = 1234

s.bind(('',port))

print("I am server in listening Mode")
s.listen(5)

connection,addr = s.accept()
print("connection from",addr)
s.recv(1024)

s.close()

input()