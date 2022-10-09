class Motor:

    def __init__(self):
        self._motor_voltage = 0.0
        self._motor_temperature = 0.0
        self._motor_warning = False
        self._speed = 0
        self._distance = 0

    def set_motor_voltage(self, m_volatge):
        self._motor_voltage = m_volatge
    def get_motor_voltage(self):
        return self._motor_voltage

    def set_motor_temperature(self, m_temp):
        self._motor_temperature = m_temp
    def get_motor_temperature(self):
        return self._motor_temperature

    def set_motor_warning(self, m_warning):
        self._motor_warning = m_warning
    def get_motor_warning(self):
        return self._motor_warning

    def set_speed(self, speed):
        self._speed = speed
    def get_speed(self):
        return self._speed

    def set_distance(self, dist):
        self._distance = dist
    def get_distance(self):
        return self._distance
