import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8888


def setup_connection_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    return client_socket


def run_client():
    client_connect = setup_connection_to_server()
    while True:
        input_text = input("Enter message: ")
        encoded_message = input_text.encode("utf-8")[:1024]
        client_connect.send(encoded_message)
        encoded_response = client_connect.recv(1024)
        response = encoded_response.decode("utf-8")
        if response.lower() == "closed":
            break
        print(f"Received: {response}")
    client_connect.close()
    print("Connection to server closed")


if __name__ == '__main__':
    run_client()
