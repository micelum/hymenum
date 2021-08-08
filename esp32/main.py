import socket
import time
from select import select
import ujson

# overwrite vars from boot.py if you need
my_wifi_mac = ''
uuid = ''

config_object = {
    "device": {
        "uuid": uuid,
        "mac": my_wifi_mac,
    }
}

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setblocking(False)

payload = ujson.dumps(config_object)

while True:  # TODO add correct condition
    sock.sendto(payload.encode('utf-8'), ('255.255.255.255', 13404))
    print("send {}".format(payload))
    is_ready = select([sock], [], [], 1)
    if is_ready[0]:
        msg, addr = sock.recvfrom(1024)
        if msg:
            try:  # TODO Add multiserver sersponse
                config = ujson.loads(msg.decode('utf-8'))
            except ValueError:
                print("unrecognized response")
                continue
            if 'septum_address' in config and config['septum_address']:  # TODO Add config to different behaviors
                config_file = open('septum_addr', 'w')
                config_file.write(config['septum_address'])
                config_file.close()
                print('septum configured successfully')
                break
    time.sleep(2)
