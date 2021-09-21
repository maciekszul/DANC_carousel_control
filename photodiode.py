import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")

it = pyfirmata.util.Iterator(board)
it.start()

board.analog[0].enable_reporting()

def lit(ix):
    board.digital[ix].write(1)
    time.sleep(0.1)
    board.digital[ix].write(0)
    time.sleep(0.1)


while True:
    pd = board.analog[0].read()
    time.sleep(0.01)
    print(pd)
    for i in [2,3,4,5,4,3]:
        pd = board.analog[0].read()
        if pd > 0.1:
            lit(i)
