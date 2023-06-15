import pygame
import random
from game.utils.constants import  ENEMY_TYPE, METEOR_1, METEOR_DESTROY, SCREEN_HEIGHT
from game.components.enemies.enemy import Enemy


class Meteor(Enemy):
    SPEED_Y = 7

    def __init__(self):
        self.image = pygame.transform.scale(METEOR_1,(30, 50))
        self.destroyed_image = pygame.transform.scale(METEOR_DESTROY, (30, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE
        self.speed_y = self.SPEED_Y


    def update(self, ships):
        self.rect.y += self.speed_y
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)
        


