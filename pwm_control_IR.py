from pyfirmata2 import Arduino
import numpy as np
import time

PORT = Arduino.AUTODETECT

samplingRate = 60

# Get the Ardunio board.
board = Arduino(PORT)

# Set the sampling rate in the Arduino
board.samplingOn(1000 / samplingRate)

pin_an_in = board.get_pin("a:0:i")
pin_an_in.enable_reporting()

pin_pwm = board.get_pin("d:3:p")
pin_pwm.write(True)

while True:
    try:
        ir = pin_an_in.read()
        if ir != None:
            mpl = int(ir*1000)
            print(">"+"|"*mpl)
        time.sleep(0.05)
    except KeyboardInterrupt:
        break

pin_pwm.write(0)
pin_an_in.disable_reporting()