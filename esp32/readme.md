# Early dev for ESP32
##### based on Mycropython

## Led indicator states
- instant light - ready
- rapid blinking - connecting to Wi-Fi network
- 1 slow blink - can`t get networks configuration
- 2 slow blinks - json config file does not exist on device
- 3 slow blinks - device can`t connect to any configured network
- 4 slow blinks - incorrect format of json file
- 5 slow blinks - 

## Dev env preparaions
### Install tools
```shell
sudo apt install picocom
pip install adafruit-ampy
```

## Load firmware to board
```shell
ampy --port /dev/ttyUSB0 put boot.py
ampy --port /dev/ttyUSB0 put main.py
```

## Connect to ESP32 REPL
```shell
picocom -b 115200 /dev/ttyUSB0
```

## Debug other services
Also, you can use `main.py` in your PC python interpreter as software debug plug
to debug without real ESP32 board

