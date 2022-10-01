from enum import IntEnum


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
