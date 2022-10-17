from serial import Serial


class SerialScanner:
    port = ''
    #ser = Serial(port)
    ser = Serial.Serial(port,
                    baudrate=9600,
					parity=Serial.PARITY_NONE,
					stopbits=Serial.STOPBITS_ONE)
    bytesToRead = ser.inWaiting()
    ser.read(bytesToRead)