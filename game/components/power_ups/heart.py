from game.components.power_ups.power_up import PowerUp
from game.utils.constants import HEART, HEART_TYPE


class Heart(PowerUp):
    def __init__(self):
        super().__init__(HEART, HEART_TYPE)
        self.type = HEART_TYPE
        self.start_time = 0
    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y