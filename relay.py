import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")

# gpios = [3, 4, 5, 6]
gpios = [6, 5, 4, 3]
# gpios = [5,3]
# gpios = [3,5, 6, 4]
while True:
    for ix in gpios:
        board.digital[ix].write(0)
        board.digital[ix].write(1)
<<<<<<< HEAD
        time.sleep(0.2)
=======
        time.sleep(0.1)
>>>>>>> 833321422b09f83029e00218b32325630e4913ba
        board.digital[ix].write(0)
