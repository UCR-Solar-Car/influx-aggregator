class TirePressure:

    def __init__(self):
        self._front_left = 0
        self._front_right = 0
        self._back_left = 0
        self._back_right = 0

    def set_front_left(self, front_left):
        self._front_left = front_left
    def get_front_left(self):
        return self._front_left

    def set_front_right(self, front_right):
        self._front_right = front_right
    def get_front_right(self):
        return self._front_right

    def set_back_left(self, back_left):
        self._back_left = back_left
    def get_back_left(self):
        return self._back_left
    
    def set_back_right(self, back_right):
        self._back_right = back_right
    def get_back_right(self):
        return self._back_right
        