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
        self.image = pygame.transform.scale(ENEMY_2, (50, 50))  # Imagen del enemigo
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)  # Posición en el eje x
        self.rect.y = self.Y_POS  # Posición en el eje y
        self.type = ENEMY_TYPE  # Tipo de enemigo

        self.speed_x = self.SPEED_X  # Velocidad en el eje x
        self.speed_y = self.SPEED_Y  # Velocidad en el eje y

        self.movement = random.choice(self.MOVEMENTS)  # Dirección de movimiento
        self.move_x = random.randint(10, 10)  # Cantidad de movimiento en el eje x
        self.moving_index = 0  # Índice de movimiento

        self.shooting_time = random.randint(30, 50)  # Tiempo entre disparos

    def update_movement(self):
        """Actualiza el movimiento del enemigo cambiando su dirección y posición."""
        self.moving_index += 1
        if self.rect.x >= SCREEN_WIDTH - 50:
            self.movement = LEFT
        elif self.rect.x <= 0:
            self.movement = RIGHT

        if self.moving_index >= self.move_x:
            self.moving_index = 0
            self.movement = LEFT if self.movement == RIGHT else RIGHT
