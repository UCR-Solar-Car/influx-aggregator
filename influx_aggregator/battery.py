class Battery:

    def __init__(self):
        self.battery_voltage = 0.0
        self.battery_temperature = 0.0
        self.battery_warning = False
        self.bps_fault = False
        self.automatic_power_opening: False
        self.range = 0.0
        