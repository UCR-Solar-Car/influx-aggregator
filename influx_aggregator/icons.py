from enum import IntEnum

class Gears(IntEnum):
    PARKING = 1
    DRIVE = 2
    NEUTRAL = 3
    REVERSE = 4

class Icons:

    def __init__(self):
        self._left_indicator : bool = False
        self._right_indicator : bool = False
        self._day_lights : bool = False
        self._night_lights : bool = False
        self._horn : bool = False
        self._cruise_control : bool = False
        self._gears : Gears = Gears.PARKING

    def set_left_indicator(self, l_indicator) -> None:
        self._left_indicator = l_indicator

    def get_left_indicator(self) -> bool:
        return self._left_indicator

    def set_right_indicator(self, r_indicator) -> None:
        self._right_indicator = r_indicator

    def get_right_indicator(self) -> bool:
        return self._right_indicator

    def set_day_lights(self, d_lights) -> None:
        self._day_lights = d_lights

    def get_day_lights(self) -> bool:
        return self._day_lights

    def set_night_lights(self, n_lights) -> None:
        self._night_lights = n_lights

    def get_night_lights(self) -> bool:
        return self._night_lights

    def set_horn(self, horn) -> None:
        self._horn = horn

    def get_horn(self) -> bool:
        return self._horn

    def set_cruise_control(self, c_control) -> None:
        self._cruise_control = c_control

    def get_cruise_control(self) -> bool:
        return self._cruise_control

    def set_gears(self, gear) -> None:
        self._gears = gear

    def get_gears(self) -> Gears:
        return self._gears
