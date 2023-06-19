from game.components.power_ups.power_up import PowerUp
from game.utils.constants import SHIELD, SHIELD_TYPE


class Shield(PowerUp):
    def __init__(self):
        super().__init__(SHIELD, SHIELD_TYPE)
        self.type = SHIELD_TYPE
        self.start_time = 0
        

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

    