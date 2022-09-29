from datetime import datetime 
from enum import IntEnum

class Payload:
    def __init__(self):
        self.uid = ""
        self.timestamp = datetime.now()
        self.motor = Motor()
        self.battery = Battery()
        self.tire_pressure = TirePressure()
        self.icons = Icons()

class Motor:
    def __init__(self):
        self.motor_voltage = 0.0
        self.motor_temperature = 0.0
        self.motor_warning = False
        self.speed = 0
        self.distance = 0

class Battery:
    def __init__(self):
        self.battery_voltage = 0.0
        self.battery_temperature = 0.0
        self.battery_warning = False
        self.bps_fault = False
        self.automatic_power_opening: False
        self.range = 0.0

class TirePressure:
    def __init__(self):
        self.front_left = 0
        self.front_right = 0
        self.back_left = 0
        self.back_right = 0

class Icons:
    def __init__(self):
        self.left_indicator = False
        self.right_indicator = False
        self.day_lights = False
        self.night_lights = False
        self.horn = False
        self.cruise_control = False
        self.gears = Gears.PARKING

class Gears(IntEnum):
    PARKING = 1
    DRIVE = 2
    NEUTRAL = 3
    REVERSE = 4