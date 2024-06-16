# Interactive Process and Networking Monitoring

## Research

If you need fast IPC between two processes on one machine, you should look into pipes or shared memory.

- https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing

### Pipes

The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way). For example:

```python
from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()
```

The two connection objects returned by Pipe() represent the two ends of the pipe. Each connection object has send() and recv() methods (among others). Note that data in a pipe may become corrupted if two processes (or threads) try to read from or write to the same end of the pipe at the same time. Of course there is no risk of corruption from processes using different ends of the pipe at the same time.


### Shared memory

Data can be stored in a shared memory map using Value or Array.

```python
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
```

## Links

- https://docs.python.org/3/library/ipc.html
- https://docs.python.org/3/howto/sockets.html

Anthology development and API

Information on how to programmatically access Anthology data https://www.aclweb.org/anthology/info/development/

AAAI Digital Library

The AAAI Library contains a number of high-quality proceedings in the field of artificial intelligence. https://aaai.org/Library/conferences-library.php 
