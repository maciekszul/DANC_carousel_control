import pyfirmata
import time
import numpy as np

board = pyfirmata.Arduino("/dev/ttyACM0")
board.analog[0].enable_reporting()
it = pyfirmata.util.Iterator(board)
it.start()

while True:
    board.digital[2].write(1)
    try:
        pd = board.analog[0].read()
        print(pd)
        time.sleep(0.05)
    except KeyboardInterrupt:
        board.digital[2].write(0)
        print("ki")
        break

