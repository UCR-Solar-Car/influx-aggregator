class TirePressure:

    def __init__(self):
        self._front_left: int = 0
        self._front_right: int = 0
        self._back_left: int = 0
        self._back_right: int = 0

    def set_front_left(self, front_left) -> None:
        self._front_left = front_left

    def get_front_left(self) -> int:
        return self._front_left

    def set_front_right(self, front_right) -> None:
        self._front_right = front_right

    def get_front_right(self) -> int:
        return self._front_right

    def set_back_left(self, back_left) -> None:
        self._back_left = back_left

    def get_back_left(self) -> int:
        return self._back_left

    def set_back_right(self, back_right) -> None:
        self._back_right = back_right

    def get_back_right(self) -> int:
        return self._back_right
