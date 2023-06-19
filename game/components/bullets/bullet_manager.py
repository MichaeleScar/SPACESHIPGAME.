import pygame
from game.components.bullets.bullet import Bullet
from game.utils.constants import ENEMY_DESTROY, ENEMY_TYPE, METEOR_DESTROY, PLAYER_TYPE, SHIELD_TYPE, SPACESHIP_DESTROY


class BulletManager:
    def __init__(self):
        self.player_bullets: list[Bullet] = []  # Lista de balas disparadas por el jugador
        self.enemy_bullets: list[Bullet] = []  # Lista de balas disparadas por los enemigos
        self.dead_player_sound = pygame.mixer.Sound("game/assets/Sounds/dead_players_sound.ogg")  # Sonido de jugador muerto
        self.enemy_dead = pygame.mixer.Sound("game/assets/Sounds/enemy_dead.ogg")  # Sonido de enemigo muerto
        self.enemy_bullet = pygame.mixer.Sound("game/assets/Sounds/enemy_bullet.ogg")  # Sonido de bala enemiga

    def update(self, game):
        #Actualiza las balas y verifica las colisiones con los jugadores y enemigos.
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets, game.player)
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                if not game.player.has_power_up or game.player.power_up_type != SHIELD_TYPE:
                    game.death_count += 1
                    self.dead_player_sound.play()
                    game.playing = False
                break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets, game.enemy_manager.enemies + game.enemy_manager.enemies_2 + game.enemy_manager.meteors)

            # Verificar colisiones con enemigos
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    if bullet in self.player_bullets:
                        self.player_bullets.remove(bullet)
                    if enemy in game.enemy_manager.enemies:
                        game.enemy_manager.enemies.remove(enemy)
                        game.score += 1
                        self.enemy_dead.play()
                    break

            for enemy_2 in game.enemy_manager.enemies_2:
                if bullet.rect.colliderect(enemy_2.rect):
                    if bullet in self.player_bullets:
                        self.player_bullets.remove(bullet)
                    if enemy_2 in game.enemy_manager.enemies_2:
                        game.enemy_manager.enemies_2.remove(enemy_2)
                        game.score += 1
                        self.enemy_dead.play()
                    break
                
            for meteor in game.enemy_manager.meteors:
                if bullet.rect.colliderect(meteor.rect):
                    if bullet in self.player_bullets:
                        self.player_bullets.remove(bullet)
                    if meteor in game.enemy_manager.meteors:
                        game.enemy_manager.meteors.remove(meteor)
                        game.score += 1
                        self.enemy_dead.play()
                    break

    def draw(self, screen):
        #Dibuja las balas en la pantalla.
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.player_bullets:
            bullet.draw(screen)
    def add_bullet(self, bullet):
        #Agrega una bala a la lista correspondiente.
        self.enemy_bullet_sound_played = False
        if bullet.owner == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(bullet)
            if not self.enemy_bullet_sound_played:
                self.enemy_bullet.play()
                self.enemy_bullet_sound_played = True
        if bullet.owner == PLAYER_TYPE:
            # Limitar a cuatro balas del jugador en pantalla
            if len(self.player_bullets) < 4:
                self.player_bullets.append(bullet)


    def reset(self):
        #Restablece las listas de balas.
        self.player_bullets = []
        self.enemy_bullets = []
