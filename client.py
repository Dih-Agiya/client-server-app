import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost (same as server)
PORT = 56789        # Port to connect to (must match server)

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))  # Connect to server

# Receive response
response = client_socket.recv(1024).decode('utf-8')
print(f"Server says: {response}")

# Close connection
client_socket.close()
