import pygame
import random
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
from game.components.enemies.enemy import Enemy



LEFT = "left"
RIGHT = "right"

class Enemy_2(Enemy):
    SPEED_X = 10
    SPEED_Y = 5
    

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_2,(50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)
        self.rect.y = self.Y_POS
        self.type = ENEMY_TYPE

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y

        self.movement = random.choice(self.MOVEMENTS)
        self.move_x = random.randint(10, 10)
        self.moving_index = 0

        self.shooting_time = random.randint(30, 50)


    def updatee_movement(self):
        self.moving_index += 1
        if self.rect.x >= SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if  self.movement == RIGHT else RIGHT