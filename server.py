import socket


def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    # The bind() function takes tuple as argument
    server_socket.bind((host, port))

    # configure how many clients the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()


if __name__ == '__main__':
    server_program()
