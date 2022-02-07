import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")

# gpios = [3, 4, 5, 6]
gpios = [6, 5, 4, 3]

while True:
    for ix in gpios:
        board.digital[ix].write(0)
        board.digital[ix].write(1)
        time.sleep(5)
        board.digital[ix].write(0)
