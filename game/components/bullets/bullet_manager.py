import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
from game.components.enemies.meteor import Meteor
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_TYPE, PLAYER_TYPE


class BulletManager:

    def __init__(self):
        self.player_bullets: list[Bullet] = []
        self.enemy_bullets: list[Bullet] =[]


    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets, game.player)
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                game.playing = False
                pygame.time.delay(1000)
                break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets, game.enemy_manager.enemies + game.enemy_manager.enemies_2 + game.enemy_manager.meteors)
            for enemy in game.enemy_manager.enemies:
                if pygame.sprite.collide_rect(bullet, enemy):
                    if bullet in self.player_bullets:
                        self.player_bullets.remove(bullet)
                    if enemy in game.enemy_manager.enemies:
                        game.enemy_manager.enemies.remove(enemy)
                    break
            for enemy_2 in game.enemy_manager.enemies_2:
                if pygame.sprite.collide_rect(bullet, enemy_2):
                    if bullet in self.player_bullets:
                        self.player_bullets.remove(bullet)
                    if enemy_2 in game.enemy_manager.enemies_2:
                        game.enemy_manager.enemies_2.remove(enemy_2)
                    break
            for meteor in game.enemy_manager.meteors:
                if pygame.sprite.collide_rect(bullet, meteor):
                    if bullet in self.player_bullets:
                        self.player_bullets.remove(bullet)
                    if meteor in game.enemy_manager.meteors:
                        game.enemy_manager.meteors.remove(meteor)
                    break



            #verificar si hemos chocado al jugador
        

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
        if bullet.owner == PLAYER_TYPE:
            self.player_bullets.append(bullet)