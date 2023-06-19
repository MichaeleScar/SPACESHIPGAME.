import pygame
import random
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_1, ENEMY_DESTROY, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

LEFT = "left"
RIGHT = "right"

class Enemy(Sprite):
    MOVEMENTS = [LEFT, RIGHT]
    X_POS_LIST = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900]
    Y_POS = -50
    SPEED_X = 5
    SPEED_Y = 1

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_1, (50, 50))  # Imagen del enemigo
        self.rect = self.image.get_rect()
        self.rect.x = random.choice(self.X_POS_LIST)  # Posición en el eje x
        self.rect.y = self.Y_POS  # Posición en el eje y
        self.type = ENEMY_TYPE  # Tipo de enemigo

        self.speed_x = self.SPEED_X  # Velocidad en el eje x
        self.speed_y = self.SPEED_Y  # Velocidad en el eje y

        self.movement = random.choice(self.MOVEMENTS)  # Dirección de movimiento
        self.move_x = random.randint(30, 100)  # Cantidad de movimiento en el eje x
        self.moving_index = 0  # Índice de movimiento

        self.shooting_time = random.randint(100, 150)  # Tiempo entre disparos

    def update(self, ships, game):
        """
        Actualiza la posición del enemigo y realiza acciones como disparar.

        """
        self.rect.y += self.speed_y
        self.shoot(game.bullet_manager)

        if self.movement == LEFT:
            self.rect.x -= self.speed_x
        else:
            self.rect.x += self.speed_x
        self.update_movement()

        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

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

    def draw(self, screen):
        """
        Dibuja el enemigo en la pantalla.
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        """Realiza un disparo creando una bala y agregándola al administrador de balas."""
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet = Bullet(self)
            bullet_manager.add_bullet(bullet)
            self.shooting_time += random.randint(100, 150)

    def set_image(self, size, image):
        """
        Establece la imagen del enemigo con un tamaño específico.

        """
        self.image = image
        self.image = pygame.transform.scale(self.image, size)
