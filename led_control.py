import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")

while True:
    for i in [2,3,4,5,4,3]:
        board.digital[i].write(1)
        time.sleep(0.1)
        board.digital[i].write(0)
        time.sleep(0.1)

