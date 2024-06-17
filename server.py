import socketserver

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8888
MESSAGE_RESPONSE = "Message Acknowledged"


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def setup(self):
        print(f"New client connected: {self.client_address}")

    def handle(self):
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            self.client_interaction(data)

    def client_interaction(self, data):
        response = data.decode("utf-8")
        print(f"Received: {response}")
        msg_to_send = MESSAGE_RESPONSE
        self.request.sendall(msg_to_send.encode("utf-8"))

    def finish(self):
        print(f"Client disconnected: {self.client_address}")


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def start_server():
    server = ThreadedTCPServer((SERVER_IP, SERVER_PORT), ThreadedTCPRequestHandler)
    print(f"Starting Server: {SERVER_IP}:{SERVER_PORT}")
    with server:
        server.serve_forever()


if __name__ == "__main__":
    start_server()
