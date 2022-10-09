from enum import IntEnum


class Icons:

    def __init__(self):
        self._left_indicator = False
        self._right_indicator = False
        self._day_lights = False
        self._night_lights = False
        self._horn = False
        self._cruise_control = False
        self._gears = Gears.PARKING

    def set_left_indicator(self, l_indicator):
        self._left_indicator = l_indicator
    def get_left_indicator(self):
        return self._left_indicator

    def set_right_indicator(self, r_indicator):
        self._right_indicator = r_indicator
    def get_right_indicator(self):
        return self._right_indicator

    def set_day_lights(self, d_lights):
        self._day_lights = d_lights
    def get_day_lights(self):
        return self._day_lights

    def set_night_lights(self, n_lights):
        self._night_lights = n_lights
    def get_night_lights(self):
        return self._night_lights

    def set_horn(self, horn):
        self._horn = horn
    def get_horn(self):
        return self._horn

    def set_cruise_control(self, c_control):
        self._cruise_control = c_control
    def get_cruise_control(self):
        return self._cruise_control

    def set_gears(self, gear):
        self._gears = gear
    def get_gears(self):
        return self._gears

class Gears(IntEnum):
    PARKING = 1
    DRIVE = 2
    NEUTRAL = 3
    REVERSE = 4
