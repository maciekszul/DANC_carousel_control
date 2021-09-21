import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")

it = pyfirmata.util.Iterator(board)
it.start()

def lit(ix, T):
    board.digital[ix].write(1)
    time.sleep(T)
    board.digital[ix].write(0)
    time.sleep(T)

while True:
    lit(2, 0.01)
    # lit(3, 0.01)
    # lit(4, 0.1)
    # lit(5, 0.2)
    time.sleep(0.4)