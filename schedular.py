import time
import socket
from random import randrange
import schedule

SERVER_IP = "127.0.0.1"
SERVER_PORT = 8888
jobs = [
    "python examples/event.py 1",
    "python examples/event.py 2",
    "python examples/event.py 3",
    "python examples/event.py 4",
    "python examples/event.py 5",
    "python examples/event.py 6",
    "python examples/event.py 7",
    "python examples/event.py 8",
    "python examples/event.py 9",
    "python examples/event.py 10"
]


def job():
    client_connect = setup_connection_to_server()
    print(*jobs, sep='\n')
    for j in jobs:
        time.sleep(randrange(1, 6))
        encoded_message = j.encode("utf-8")[:1024]
        client_connect.send(encoded_message)
        encoded_response = client_connect.recv(1024)
        response = encoded_response.decode("utf-8")
    client_connect.close()
    print("Connection to server closed")


def setup_connection_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))
    return client_socket


def run_client():
    common_time = "03:01"
    schedule.every().monday.at(common_time).do(job)
    schedule.every().tuesday.at(common_time).do(job)
    schedule.every().wednesday.at(common_time).do(job)
    schedule.every().thursday.at(common_time).do(job)
    schedule.every().friday.at(common_time).do(job)
    while True:
        time.sleep(randrange(1, 6))
        schedule.run_pending()


if __name__ == '__main__':
    run_client()
