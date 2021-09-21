import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")

gpios = [3, 4, 5, 6]

while True:
    for ix in gpios:
        board.digital[ix].write(0)
        board.digital[ix].write(1)
        time.sleep(1)
        board.digital[ix].write(0)