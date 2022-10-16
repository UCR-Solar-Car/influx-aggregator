class Motor:

    def __init__(self):
        self._motor_voltage: float = 0.0
        self._motor_temperature: float = 0.0
        self._motor_warning: bool = False
        self._speed: int = 0
        self._distance: int = 0

    def set_motor_voltage(self, m_volatge) -> None:
        self._motor_voltage = m_volatge

    def get_motor_voltage(self) -> float:
        return self._motor_voltage

    def set_motor_temperature(self, m_temp) -> None:
        self._motor_temperature = m_temp

    def get_motor_temperature(self) -> float:
        return self._motor_temperature

    def set_motor_warning(self, m_warning) -> None:
        self._motor_warning = m_warning

    def get_motor_warning(self) -> bool:
        return self._motor_warning

    def set_speed(self, speed) -> None:
        self._speed = speed

    def get_speed(self) -> int:
        return self._speed

    def set_distance(self, dist) -> None:
        self._distance = dist

    def get_distance(self) -> int:
        return self._distance
