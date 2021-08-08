import network
import time
import ubinascii
import ujson
import os
from machine import Pin, reset

status_pin = Pin(5, Pin.OUT)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

root_dir_listing = os.listdir()
# Read config from config.json
if 'config.json' in root_dir_listing:
    config_file = open('config.json', 'r')
    raw_config = config_file.read()
    config_file.close()
    try:
        config = ujson.loads(raw_config.replace('\n', ''))
    except ValueError:
        print('Incorrect format of json file')
        while True:
            status_pin.off()
            time.sleep(2)
            for x in range(0, 4):
                status_pin.on()
                time.sleep_ms(500)
                status_pin.off()
                time.sleep_ms(500)
else:
    print('Json config file does not exist')
    while True:
        status_pin.off()
        time.sleep(2)
        for x in range(0, 2):
            status_pin.on()
            time.sleep_ms(500)
            status_pin.off()
            time.sleep_ms(500)

if 'wifi' in config and len(config['wifi']):
    for wifi_ssid, wifi_password in config['wifi'].items():
        my_wifi_mac = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
        if not wlan.isconnected():
            print(my_wifi_mac, 'connecting to network', wifi_ssid)
            connect_attempt = 0
            wlan.connect(wifi_ssid, wifi_password)
            while not wlan.isconnected() and connect_attempt < 10:
                connect_attempt = connect_attempt + 1
                print("Attempt", connect_attempt)
                for x in range(1, 5):  # TODO add function for this
                    status_pin.on()
                    time.sleep_ms(100)
                    status_pin.off()
                    time.sleep_ms(100)
                time.sleep_ms(300)
            if wlan.isconnected():
                print('Connected to network', wifi_ssid)
                print('Network config:', wlan.ifconfig())
                status_pin.on()
                break
            else:
                print('Connection to network', wifi_ssid, 'is not successful.')
                wlan.disconnect()
    if not wlan.isconnected():
        print('Device can`t connect to any configured network.')
        while True:
            status_pin.off()
            time.sleep(2)
            for x in range(0, 3):
                status_pin.on()
                time.sleep_ms(500)
                status_pin.off()
                time.sleep_ms(500)
else:
    print('Cant get networks configuration.')
    while True:
        status_pin.off()
        time.sleep(2)
        for x in range(0, 1):
            status_pin.on()
            time.sleep_ms(500)
            status_pin.off()
            time.sleep_ms(500)

# Check is this boot initial
if 'uuid' not in root_dir_listing:
    print('UUID file not found. Initialising...')
    import urequests
    uuid_request = urequests.get('https://www.uuidtools.com/api/generate/v4')
    uuid = uuid_request.json()[0]
    print('Get new UUID', uuid)
    uuid_file = open('uuid', 'w')
    uuid_file.write(uuid)
    uuid_file.close()

uuid_file = open('uuid', 'r')
uuid = uuid_file.read()
uuid_file.close()
if not uuid:
    print('UUID file is empty. Remove it and reset')
    os.remove('uuid')
    reset()

# TODO Add OTA

