import os
import time
import socket
import threading
from datetime import datetime
from collections import defaultdict

processes = defaultdict(str)

ct = datetime.now()
print("current time:", ct)

ts = ct.timestamp()
print("timestamp:", ts)

ipc_var = ''


def thread_function():
    global ipc_var

    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        else:
            print("received: " + str(data))
            ipc_var = str(data)
    conn.close()


x = threading.Thread(target=thread_function)
x.start()

while True:
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    current_state = defaultdict(str)
    for pid in pids:
        try:
            proc = open(os.path.join('/proc', pid, 'cmdline'), 'rb')
            for line in proc.readlines():
                current_state[pid] = line.strip().decode()
        except IOError:
            continue

    new_state_message = True
    for p in current_state:
        if processes[p] == '':
            if new_state_message:
                ct = time.time()
                dt_object = datetime.fromtimestamp(ct)
                print("New Process Detected", dt_object)
            processes[p] = current_state[p]
            print("\t", p, processes[p])
            new_state_message = False

    new_state_message = True
    proc_ended = []
    for p in processes:
        if processes[p] != current_state[p]:
            if new_state_message:
                ct = time.time()
                dt_object = datetime.fromtimestamp(ct)
                print("Process Ended", dt_object)
            print("\t", p, processes[p])
            proc_ended.append(p)
            new_state_message = False
    for p in proc_ended:
        del processes[p]

    time.sleep(5)
