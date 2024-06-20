import subprocess
import socketserver
import threading
from random import randrange
import time
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8888
BUFFER_SIZE = 1024
CLOSE_COMMAND = 'close'
CLOSED_RESPONSE = 'closed'
ACCEPTED_RESPONSE = 'accepted'
ENCODING = 'utf-8'
EXIT = False
QUEUE = []


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        client = f"{self.client_address[0]}:{self.client_address[1]}"
        print(f"Accepted connection from {client}")
        while True:
            try:
                request_data = self.request.recv(BUFFER_SIZE)
            except Exception as e:
                print(f"{client} Connection aborted unexpectedly: {e}")
                break
            request_data = request_data.decode(ENCODING)
            if request_data.lower() == CLOSE_COMMAND:
                self.request.send(CLOSED_RESPONSE.encode(ENCODING))
                break
            print(f"{client}\t{request_data}")
            self.request.send(ACCEPTED_RESPONSE.encode(ENCODING))
            try:
                cmd_tokens = request_data.split(' ')
                if cmd_tokens[0] == "python":
                    QUEUE.append(cmd_tokens)
            except IndexError:
                print(f"Invalid command: {request_data}")


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def proc_queue():
    while True:
        time.sleep(randrange(1, 3))
        if EXIT:
            os._exit(0)
        if len(QUEUE) > 0:
            print(f"Number of commands in the QUEUE is: {len(QUEUE)}")
            print(*QUEUE, sep='\n')
            cmd = QUEUE.pop(0)
            print(f"Processing item: {cmd}")
            result = subprocess.run(cmd)


if __name__ == '__main__':
    queue_thread = threading.Thread(target=proc_queue)
    queue_thread.start()
    server = ThreadedTCPServer((SERVER_IP, SERVER_PORT), ThreadedTCPRequestHandler)
    print(f"Listening on {SERVER_IP}:{SERVER_PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Server is shutting down due to manual interrupt...")
    EXIT = True
