import socket
from config import PORT, HOST
from core.parser import parse_request

# 1. socket() -> 2. bind() -> 3. listen() -> 4. accept() -> 5. recv() -> 6. send() -> 7. close()


def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket 
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()  # socket object, address info
        print(f"New connection from {client_address}")

        raw_request = client_socket.recv(4096).decode()

        print("Before parser")

        request = parse_request(raw_request)

        print("After parser")

        print(f"Method : {request.method}")
        print(f"Path   : {request.path}")
        print(f"Version: {request.version}")
        print(f"Headers: {request.headers}")
        print(f"Query  : {request.query_params}")
        print(f"Body   : {request.body}")

        client_socket.close()

       # response = router.handle(request)

      #  client_socket.send(response.to_bytes())

if __name__ == "__main__":
    start_server()