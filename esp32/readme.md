# Early dev for ESP32
##### based on Mycropython

##Dev env preparaions
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
