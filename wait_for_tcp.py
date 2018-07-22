import socket
from sys import argv
from time import sleep, time

if len(argv) != 4:
    desc = """
python wait_for_tcp host port timeout
"""
    print(desc)
    exit(1)

host = argv[1]
port = int(argv[2])
timeout = int(argv[3])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ok = False
start = time()
while not ok:
    try:
        client.connect((host, port))
        ok = True
    except ConnectionRefusedError:
        pass
    finally:
        if ok:
            client.close()
        else:
            sleep(1)
        elapsed_time = time() - start
        if elapsed_time >= timeout:
            break

exit(0 if ok else 1)
