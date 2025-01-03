import socket

# Create a socket object
client_socket = socket.socket()

# Define server IP and port
server_ip = '192.168.1.143'  # Replace with your server's IP
server_port = 6341

# Connect to the server
client_socket.connect((server_ip, server_port))
print("Connected to the server.")

while True:
    # Send a message to the server
    client_message = input("You: ")
    client_socket.send(client_message.encode())
    if client_message.lower() == "exit":
        print("Disconnecting from the server.")
        break

    # Receive message from the server
    server_message = client_socket.recv(1024).decode()
    if server_message.lower() == "exit":
        print("Server has closed the connection.")
        break
    print(f"Server: {server_message}")

client_socket.close()
