import os

pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
processes = []
for pid in pids:
    try:
        proc = open(os.path.join('/proc', pid, 'cmdline'), 'rb')
        Lines = proc.readlines()
        print(Lines)
        for line in Lines:
            line = line.strip().decode()
            if len(line) > 0:
                processes.append(line)
    except IOError:
        continue


for p in processes:
    print(p)

