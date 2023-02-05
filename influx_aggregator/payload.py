from datetime import datetime
from motor import Motor
from battery import Battery
from tire_pressure import TirePressure
from icons import Icons

#pylint: skip-file


class Payload:

    def __init__(self):
        self.uid = ""
        self.timestamp = datetime.now()
        self.motor = Motor()
        self.battery = Battery()
        self.tire_pressure = TirePressure()
        self.icons = Icons()
