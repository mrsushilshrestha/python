import socket

# Create a socket object
server_socket = socket.socket()

# Define server IP and port
server_ip = '192.168.1.65'  # Replace with your server's IP
server_port = 6341

# Bind the socket to the address and port
server_socket.bind((server_ip, server_port))

print("Server is waiting for a connection...")
server_socket.listen(5)

# Accept a connection
connection, addr = server_socket.accept()
print(f"Connected to client at {addr}")

while True:
    # Receive message from the client
    client_message = connection.recv(1024).decode()
    if client_message.lower() == "exit":
        print("Client has disconnected.")
        break
    print(f"Client: {client_message}")
    
    # Send a message to the client
    server_message = input("You: ")
    connection.send(server_message.encode())
    if server_message.lower() == "exit":
        print("Closing connection.")
        break

connection.close()
server_socket.close()
