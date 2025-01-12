import socket

s= socket.socket()

port = 6341

s.bind(('192.168.1.65',port))

print("I am server in listening Mode")
s.listen(5)

connection,addr = s.accept()
print("connection from",addr)

message = connection.recv(1024)
print(message)

# s.recv(1024)

s.close()

input()