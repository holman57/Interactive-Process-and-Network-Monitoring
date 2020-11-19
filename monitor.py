import os
import time
from datetime import datetime
from collections import defaultdict

ct = datetime.now()
print("current time:", ct)

ts = ct.timestamp()
print("timestamp:", ts)

processes = defaultdict(str)


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
