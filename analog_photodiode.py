import pyfirmata
import time
import numpy as np

board = pyfirmata.Arduino("/dev/ttyACM0")

it = pyfirmata.util.Iterator(board)
it.start()
t0 = time.time()
board.analog[0].enable_reporting()
time_count = []
photodiode_level = []
while True:
    try:
        pd = board.analog[0].read()
        t = time.time() - t0
        time_count.append(t)
        photodiode_level.append(pd)
        print(pd)
        time.sleep(0.1)
    except KeyboardInterrupt:
        print("ki")
        break

out = np.vstack([np.array(time_count), np.array(photodiode_level)])
np.save("time_pd.npy", out)