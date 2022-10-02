class Battery:

    def __init__(self):
        self.__battery_voltage = 0.0
        self.__battery_temperature = 0.0
        self.__battery_warning = False
        self.__bps_fault = False
        self.__automatic_power_opening: False
        self.__range = 0.0

    def set_voltage(self, voltage):
        self.battery_voltage = voltage
    def get_voltage(self):
        return self.battery_voltage

    def set_temperature(self, temp):
        self.battery_temperature = temp
    def get_temperature(self):
        return self.battery_temperature

    def set_warning(self, warning):
        self.battery_warning = warning
    def get_warning(self):
        return self.battery_warning

    def set_bps_fault(self, fault):
        self.bps_fault = fault
    def get_bps_fault(self):
        return self.bps_fault

    def set_automatic_power_opening(self, apo):
        self.automatic_power_opening = apo
    def get_automatic_power_opening(self):
        return self.automatic_power_opening

    def set_range(self, range):
        self.range = range
    def get_range(self):
        return self.range