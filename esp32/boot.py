import network
import time
import ubinascii
from machine import Pin

wifi_ssid = ''  # TODO add reading from file
wifi_password = ''  # TODO add reading from file

status_pin = Pin(5, Pin.OUT)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)


if not wlan.isconnected():
    my_wifi_mac = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
    print(my_wifi_mac, 'connecting to network', wifi_ssid)
    wlan.connect(wifi_ssid, wifi_password)
    for x in range(1, 2):  # TODO add function for this
        status_pin.off()
        time.sleep_ms(250)
        status_pin.on()
        time.sleep_ms(250)
    count = 0
    while not wlan.isconnected() and count < 10:
        for x in range(1, 5):  # TODO add function for this
            status_pin.off()
            time.sleep_ms(100)
            status_pin.on()
        count = count + 1
        time.sleep_ms(500)
    print('Connected to network', wifi_ssid, end='. ')
    print('Network config:', wlan.ifconfig())
