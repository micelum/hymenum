import socket
import time
from select import select

count = 0

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(0)

while True:
    sock.sendto(b'ololo micropy {}'.format(count), ('255.255.255.255', 404))
    print("send {}".format(count))

    is_ready = select([sock], [], [], 1)
    if is_ready[0]:
        msg, addr = sock.recvfrom(1024)
        if msg:
            print("rcv: ", msg, addr)
    time.sleep(2)
    count = count + 1
