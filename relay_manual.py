import pyfirmata
import time

board = pyfirmata.Arduino("/dev/ttyACM0")


gpios_dict = {
    "1": 3,
    "2": 4,
    "3": 5,
    "4": 6
}

for ix in gpios_dict.keys():
    board.digital[gpios_dict[ix]].write(0)

while True:
    val = input()
    if str(val) == "1":
        board.digital[gpios_dict[str(val)]].write(1)
        time.sleep(0.5)
        board.digital[gpios_dict[str(val)]].write(0)
    if str(val) == "2":
        board.digital[gpios_dict[str(val)]].write(1)
        time.sleep(0.5)
        board.digital[gpios_dict[str(val)]].write(0)
    if str(val) == "3":
        board.digital[gpios_dict[str(val)]].write(1)
        time.sleep(0.5)
        board.digital[gpios_dict[str(val)]].write(0)
    if str(val) == "4":
        board.digital[gpios_dict[str(val)]].write(1)
        time.sleep(0.5)
        board.digital[gpios_dict[str(val)]].write(0)
    if str(val) == "`":
        break
