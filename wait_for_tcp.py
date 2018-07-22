import socket
from sys import argv
from time import sleep, time

if len(argv) != 4:
    desc = """
python wait_for_tcp host port timeout
"""
    print(desc)
    exit(1)

try:
    _ = ConnectionRefusedError
except NameError:
    ConnectionRefusedError = socket.error

host = argv[1]
port = int(argv[2])
timeout = int(argv[3])

ok = False
start = time()
while not ok:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((host, port))
        ok = True
    except ConnectionRefusedError:
        pass
    finally:
        client.close()
        if not ok:
            elapsed_time = time() - start
            if elapsed_time >= timeout:
                break

exit(0 if ok else 1)
