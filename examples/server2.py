import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8888
BUFFER_SIZE = 1024
CLOSE_COMMAND = 'close'
CLOSED_RESPONSE = 'closed'
ACCEPTED_RESPONSE = 'accepted'
ENCODING = 'utf-8'


def init_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(0)
    print(f"Listening on {SERVER_IP}:{SERVER_PORT}")
    return server_socket


def process_request(client_socket):
    while True:
        request_data = client_socket.recv(BUFFER_SIZE)
        request_data = request_data.decode(ENCODING)
        if request_data.lower() == CLOSE_COMMAND:
            client_socket.send(CLOSED_RESPONSE.encode(ENCODING))
            break
        print(f"Received: {request_data}")
        client_socket.send(ACCEPTED_RESPONSE.encode(ENCODING))


def run_server():
    server_socket = init_server()
    try:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        process_request(client_socket)
    except KeyboardInterrupt:
        print("Server is shutting down due to manual interrupt...")
    finally:
        if 'client_socket' in locals():
            client_socket.close()
            print("Connection to client closed")
        server_socket.close()
        print("Server socket closed")


if __name__ == '__main__':
    run_server()
