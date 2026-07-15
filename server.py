import socket
from config import PORT, HOST

# 1. socket() -> 2. bind() -> 3. listen() -> 4. accept() -> 5. recv() -> 6. send() -> 7. close()


def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket 
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()  # socket object, address info
        print(f"New connection from {client_address}")

        request = client_socket.recv(1024) # receive data from the client, upto 1024 bytes
        print("Raw Request:")
        print(request.decode())

        client_socket.close()


if __name__ == "__main__":
    start_server()