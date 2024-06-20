import time
import os
from random import random
import argparse


def main():
    parser = argparse.ArgumentParser(description="Preform an action for period of time")
    parser.add_argument('duration', type=int, help='accepts INT')
    args = parser.parse_args()
    pid = os.getpid()
    print(f"spawn process {pid}")
    print(f"Delay for {args.duration}")
    n = args.duration
    i = 0
    while i < n:
        wait = int(random() * 5)
        print(f"process {pid} wait for {wait}s")
        time.sleep(wait)
        i += wait
    print(f"process {pid} finished")


if __name__ == '__main__':
    main()
