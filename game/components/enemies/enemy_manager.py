import pygame
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
from game.components.enemies.meteor import Meteor
from game.utils.constants import HEART_TYPE


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []        # Lista de enemigos normales
        self.enemies_2: list[Enemy_2] = []    # Lista de enemigos de tipo 2
        self.meteors: list[Meteor] = []       # Lista de meteoritos
        self.dead_player_sound = pygame.mixer.Sound("game/assets/Sounds/dead_players_sound.ogg")
        self.enemy_dead = pygame.mixer.Sound("game/assets/Sounds/enemy_dead.ogg")
        
        self.enemy_timer = 0                   # Tiempo transcurrido desde la creación del último enemigo normal
        self.enemy_2_timer = 0                 # Tiempo transcurrido desde la creación del último enemigo de tipo 2
        self.meteor_timer = 0                  # Tiempo transcurrido desde la creación del último meteorito

        self.enemy_delay = 5000                # Retraso entre la creación de enemigos normales (en milisegundos)
        self.enemy_2_delay = 9900              # Retraso entre la creación de enemigos de tipo 2 (en milisegundos)
        self.meteor_delay = 6000               # Retraso entre la creación de meteoritos (en milisegundos)

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if current_time - self.enemy_timer >= self.enemy_delay:
            self.enemies.append(Enemy())                # Crear un nuevo enemigo normal y agregarlo a la lista
            self.enemy_timer = current_time             # Reiniciar el contador de tiempo para enemigos normales
            
        if not self.enemies_2 and current_time - self.enemy_2_timer >= self.enemy_2_delay:
            self.enemies_2.append(Enemy_2())            # Crear un nuevo enemigo de tipo 2 y agregarlo a la lista
            self.enemy_2_timer = current_time           # Reiniciar el contador de tiempo para enemigos de tipo 2

        if not self.meteors and current_time - self.meteor_timer >= self.meteor_delay:
            self.meteors.append(Meteor())               # Crear un nuevo meteorito y agregarlo a la lista
            self.meteor_timer = current_time            # Reiniciar el contador de tiempo para meteoritos

        for enemy in self.enemies:
            enemy.update(self.enemies, game)             # Actualizar el enemigo normal y pasar la lista de enemigos y el juego como argumentos
            if enemy.rect.colliderect(game.player.rect):  # Comprobar la colisión entre el enemigo normal y el jugador
                self.enemies.remove(enemy)               # Eliminar el enemigo normal de la lista
                self.enemy_dead.play()                    # Reproducir sonido de enemigo eliminado
                if not game.player.has_power_up or game.player.power_up_type != HEART_TYPE:
                    game.playing = False                   # Detener el juego si el jugador no tiene un power-up de corazón
                    game.death_count += 1                   # Incrementar el contador de muertes del jugador
                    pygame.time.delay(1000)                 # Retrasar el juego durante 1 segundo
                break

        for enemy_2 in self.enemies_2:
            enemy_2.update(self.enemies_2, game)          # Actualizar el enemigo de tipo 2 y pasar la lista de enemigos de tipo 2 y el juego como argumentos
            if enemy_2.rect.colliderect(game.player.rect): # Comprobar la colisión entre el enemigo de tipo 2 y el jugador
                self.enemies_2.remove(enemy_2)             # Eliminar el enemigo de tipo 2 de la lista
                self.enemy_dead.play()                      # Reproducir sonido de enemigo eliminado
                if not game.player.has_power_up or game.player.power_up_type != HEART_TYPE:
                    game.playing = False                     # Detener el juego si el jugador no tiene un power-up de corazón
                    game.death_count += 1                     # Incrementar el contador de muertes del jugador
                    pygame.time.delay(1000)                   # Retrasar el juego durante 1 segundo
                    self.dead_player_sound.play()              # Reproducir sonido de jugador muerto
                break

        for meteor in self.meteors:
            meteor.update(self.meteors)                    # Actualizar el meteorito y pasar la lista de meteoritos como argumento
            if meteor.rect.colliderect(game.player.rect):   # Comprobar la colisión entre el meteorito y el jugador
                self.meteors.remove(meteor)                  # Eliminar el meteorito de la lista
                self.enemy_dead.play()                        # Reproducir sonido de enemigo eliminado
                if not game.player.has_power_up or game.player.power_up_type != HEART_TYPE:
                    game.playing = False                       # Detener el juego si el jugador no tiene un power-up de corazón
                    game.death_count += 1                       # Incrementar el contador de muertes del jugador
                    pygame.time.delay(1000)                     # Retrasar el juego durante 1 segundo
                    self.dead_player_sound.play()                # Reproducir sonido de jugador muerto
                break

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)                   # Dibujar el enemigo normal en la pantalla

        for enemy_2 in self.enemies_2:
            enemy_2.draw(screen)                 # Dibujar el enemigo de tipo 2 en la pantalla

        for meteor in self.meteors:
            meteor.draw(screen)                   # Dibujar el meteorito en la pantalla

    def reset(self):
        self.enemies = []                         # Reiniciar la lista de enemigos normales
        self.enemies_2 = []                       # Reiniciar la lista de enemigos de tipo 2
        self.meteors = []                          # Reiniciar la lista de meteoritos
