import subprocess
from random import randrange


def main():
    commands = [
        "python",
        "event.py",
        f"{randrange(1, 15)}"
    ]
    result = subprocess.run(commands)
    commands = [
        "python",
        "event.py",
        f"{randrange(1, 15)}"
    ]
    result = subprocess.run(commands)


if __name__ == '__main__':
    main()
