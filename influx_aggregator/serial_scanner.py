#pylint: disable=too-few-public-methods

from serial import Serial, PARITY_NONE, STOPBITS_ONE


class SerialScanner:
    port = ''
    #ser = Serial(port)
    ser = Serial(port,
                        baudrate=9600,
                        parity=PARITY_NONE,
                        stopbits=STOPBITS_ONE)
    bytesToRead = ser.inWaiting()
    ser.read(bytesToRead)
