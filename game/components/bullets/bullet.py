import pygame
from pygame.sprite import Sprite

from game.utils.constants import BULLET, BULLET_ENEMY, ENEMY_TYPE, PLAYER_TYPE, SCREEN_HEIGHT


class Bullet(Sprite):
    SPEED = 20
    ENEMY_BULLET_IMG = pygame.transform.scale(BULLET_ENEMY, (9, 32))
    SPACESHIP_BULLET_IMG = pygame.transform.scale(BULLET, (9, 32))
    BULLETS = {ENEMY_TYPE: ENEMY_BULLET_IMG, PLAYER_TYPE: SPACESHIP_BULLET_IMG}

    def __init__(self, spaceship):
        self.image = self.BULLETS[spaceship.type]
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center
        self.owner = spaceship.type

    def update(self, bullets, enemies):
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
        screen.blit(self.image, (self.rect.x, self.rect.y))
