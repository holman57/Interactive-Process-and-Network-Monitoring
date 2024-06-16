import time
import os
from random import random


pid = os.getpid()
print(f"spawn process {pid}")
n = int(random() * 20)
i = 0
while i < n:
    wait = int(random() * 5)
    print(f"process {pid} wait for {wait}s")
    time.sleep(wait)
    i += wait
print(f"process {pid} finished")


