import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, PLAYER_TYPE, SCREEN_HEIGHT


class Bullet(Sprite):
    SPEED = 20  # Velocidad de la bala
    ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))  # Imagen de la bala enemiga
    SPACESHIP_BULLET_IMG = pygame.transform.scale(BULLET, (9, 32))  # Imagen de la bala del jugador
    BULLETS = {ENEMY_TYPE: ENEMY_BULLET_IMG, PLAYER_TYPE: SPACESHIP_BULLET_IMG}  # Diccionario de imágenes de balas

    def __init__(self, spaceship):
        super().__init__()
        self.image = self.BULLETS[spaceship.type]  # Imagen de la bala según el tipo de nave
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type  # Tipo de dueño de la bala (jugador o enemigo)

    def update(self, bullets, enemies):
        """
        Actualiza la posición de la bala y verifica colisiones con enemigos.

        Args:
            bullets: Lista de balas a la que pertenece la bala actual.
            enemies: Lista de enemigos para verificar colisiones.
        """
        if self.owner == ENEMY_TYPE:
            self.rect.y += self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                bullets.remove(self)
        if self.owner == PLAYER_TYPE:
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                bullets.remove(self)
            else:
                for enemy in enemies:
                    if self.rect.colliderect(enemy.rect):
                        bullets.remove(self)
                        enemies.remove(enemy)
                        break

    def draw(self, screen):
        """
        Dibuja la bala en la pantalla.

        Args:
            screen: Superficie de la pantalla donde se dibujará la bala.
        """
        screen.blit(self.image, (self.rect.x, self.rect.y))
