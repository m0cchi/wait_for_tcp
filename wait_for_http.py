import re
import socket
from sys import argv
from time import sleep, time



if len(argv) != 3:
    desc = """
python wait_for_tcp host port timeout
"""
    print(desc)
    exit(1)

try:
    _ = ConnectionRefusedError
except NameError:
    ConnectionRefusedError = socket.error

url = argv[1]
timeout = int(argv[2])

port = 443 if url.startswith('https://') else 80

url = re.sub(r'https?://', '', url)
url = re.sub(r'/.*$', '', url)
urlparts = url.split(':')


host = urlparts[0]
if len(urlparts) > 1:
    port = int(urlparts[1])



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
