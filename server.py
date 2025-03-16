import socket

HOST = '127.0.0.1'  # Localhost
PORT = 56789        # Port to listen on

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print(f"🚀 Server is listening on {HOST}:{PORT}...")  # Added print statement

while True:
    client_socket, client_address = server_socket.accept()
    print(f"✅ Connection from {client_address} established.")  # Added print statement

    message = "Hello, Client! Connection successful."
    client_socket.sendall(message.encode('utf-8'))

    client_socket.close()

