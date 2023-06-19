import pygame
import random
from game.utils.constants import ENEMY_TYPE, METEOR_1, METEOR_DESTROY, SCREEN_HEIGHT
from game.components.enemies.enemy import Enemy


class Meteor(Enemy):
    SPEED_Y = 7

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(METEOR_1, (30, 50))  # Imagen del meteorito
        self.destroyed_image = pygame.transform.scale(METEOR_DESTROY, (30, 50))  # Imagen cuando el meteorito es destruido
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)  # Posición en el eje x
        self.rect.y = self.Y_POS  # Posición en el eje y
        self.type = ENEMY_TYPE  # Tipo de enemigo
        self.speed_y = self.SPEED_Y  # Velocidad en el eje y

    def update(self, ships):
        """Actualiza la posición del meteorito y lo elimina si está fuera de la pantalla."""
        self.rect.y += self.speed_y
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
