import pyfirmata2
from pyfirmata2 import Arduino
import time

PORT = Arduino.AUTODETECT
board = Arduino(PORT)
samplingRate = 1000
board.samplingOn(1000 / samplingRate)

board.analog[0].enable_reporting()
board.analog[1].enable_reporting()

gpios = [3, 4, 5, 6]

s_t = 0.05

while True:
    for gpio in gpios:
        board.digital[gpio].write(0)
        board.digital[gpio].write(1)
        try:
            pd = board.analog[0].read()
            if pd == None:
                pd = 0.0
        except KeyboardInterrupt:
            board.exit()
            print("stop")
            break
        print(pd)
        if pd > 0.0:
            while True:
                try:
                    pd = board.analog[0].read()
                    if pd == None:
                        pd = 0.0
                except KeyboardInterrupt:
                    board.exit()
                    print("stop")
                    break
                print(pd)
                time.sleep(s_t)
                if pd > 0.0:
                    continue
                elif pd == 0.0:
                    break

        time.sleep(s_t)
        board.digital[gpio].write(0)

    
    #     while True:
    #         pd = 0.0
    #         try:
    #             pd = board.analog[0].read()
    #             if pd == None:
    #                 pd = 0.0
    #         except KeyboardInterrupt:
    #             board.exit()
    #             print("stop")
    #             break
    #         if pd > 0.0:
    #             continue
    #         if pd == 0.0:
    #             break
    #     print(pd)



    