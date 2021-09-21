import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[0].enable_reporting()
while True:
    print(board.analog[0].read())
    time.sleep(0.1)