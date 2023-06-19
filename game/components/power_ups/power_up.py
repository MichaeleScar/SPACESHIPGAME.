import random
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT

class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, SCREEN_HEIGHT - 120)
        self.rect.y = 0
        self.start_time = 0

    def update(self, speed, power_ups):
        """
        Actualiza la posición del power-up.
        """
        self.rect.y += speed
        if self.rect.y < 0 or self.rect.y >= SCREEN_HEIGHT:
            power_ups.remove(self)

    def draw(self, screen):
        """
        Dibuja el power-up en la pantalla.
        """
        screen.blit(self.image, self.rect)
