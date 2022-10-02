class Battery:

    def __init__(self):
        self._battery_voltage = 0.0
        self._battery_temperature = 0.0
        self._battery_warning = False
        self._bps_fault = False
        self._automatic_power_opening: False
        self._range = 0.0

        def set_voltage(self, voltage):
            self._battery_voltage = voltage
        def get_voltage(self):
            return self._battery_voltage

        def set_temperature(self, temp):
            self._battery_temperature = temp
        def get_temperature(self):
            return self._battery_temperature

        def set_warning(self, warning):
            self._battery_warning = warning
        def get_warning(self):
            return self._battery_warning

        def set_bps_fault(self, fault):
            self._bps_fault = fault
        def get_bps_fault(self):
            return self._bps_fault

        def set_automatic_power_opening(self, apo):
            self._automatic_power_opening = apo
        def get_automatic_power_opening(self):
            return self._automatic_power_opening

        def set_range(self, range):
            self._range = range
        def get_range(self):
            return self._range
