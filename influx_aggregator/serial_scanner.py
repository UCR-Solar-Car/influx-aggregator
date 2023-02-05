#pylint: disable=too-few-public-methods

import serial
import time


print(PORT)
i = 0
    
ser = serial.Serial(PORT, 9600, timeout = 5)
time.sleep(2)


# while ser.inWaiting() > 0:
#     print(ser.readline())