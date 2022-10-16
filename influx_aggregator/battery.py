class Battery:

    def __init__(self):
        self._battery_voltage: float = 0.0
        self._battery_temperature: float = 0.0
        self._battery_warning: bool = False
        self._bps_fault: bool = False
        self._automatic_power_opening: bool = False
        self._range: float = 0.0

    def set_voltage(self, voltage) -> None:
        self._battery_voltage = voltage

    def get_voltage(self) -> float:
        return self._battery_voltage

    def set_temperature(self, temp) -> None:
        self._battery_temperature = temp

    def get_temperature(self) -> float:
        return self._battery_temperature

    def set_warning(self, warning) -> None:
        self._battery_warning = warning

    def get_warning(self) -> bool:
        return self._battery_warning

    def set_bps_fault(self, fault) -> None:
        self._bps_fault = fault

    def get_bps_fault(self) -> bool:
        return self._bps_fault

    def set_automatic_power_opening(self, apo) -> None:
        self._automatic_power_opening = apo

    def get_automatic_power_opening(self) -> bool:
        return self._automatic_power_opening

    def set_range(self, reach) -> None:
        self._range = reach

    def get_range(self) -> float:
        return self._range
