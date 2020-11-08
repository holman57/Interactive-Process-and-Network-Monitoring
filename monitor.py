import os
import time
from collections import defaultdict

processes = defaultdict(str)

while True:
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    current_state = defaultdict(str)
    for pid in pids:
        try:
            proc = open(os.path.join('/proc', pid, 'cmdline'), 'rb')
            Lines = proc.readlines()
            for line in Lines:
                line = line.strip().decode()
                if len(line) > 0:
                    current_state[pid] = line
        except IOError:
            continue

    new_state_message = True
    for p in current_state:
        if processes[p] == '':
            if new_state_message:
                print("New Process Detected")
            processes[p] = current_state[p]
            print("\t", p, processes[p])
            new_state_message = False

    new_state_message = True
    proc_ended = []
    for p in processes:
        if processes[p] != current_state[p]:
            if new_state_message:
                print("Process Ended")
            print("\t", p, processes[p])
            proc_ended.append(p)
            new_state_message = False
    for p in proc_ended:
        del processes[p]

    time.sleep(5)
