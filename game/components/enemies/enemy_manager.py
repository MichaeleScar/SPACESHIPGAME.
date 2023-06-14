import time
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
from game.components.enemies.meteor import Meteor


class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.enemies_2: list[Enemy_2] = []
        self.meteors: list[Meteor] = []
        
        self.enemy_timer = 0  # Contador de tiempo para el enemigo
        self.enemy_2_timer = 0 
        self.meteor_timer = 0  

        self.enemy_delay = 5  # Tiempo de espera en segundos para el enemigo
        self.enemy_2_delay = 10 
        self.meteor_delay = 20  

    def update(self):
        current_time = time.time() 

        if current_time - self.enemy_timer >= self.enemy_delay:
            self.enemies.append(Enemy())
            self.enemy_timer = current_time  # Reiniciar el contador de tiempo

        if not self.enemies_2 and current_time - self.enemy_2_timer >= self.enemy_2_delay:
            self.enemies_2.append(Enemy_2())
            self.enemy_2_timer = current_time 

        if not self.meteors and current_time - self.meteor_timer >= self.meteor_delay:
            self.meteors.append(Meteor())
            self.meteor_timer = current_time  

        for enemy in self.enemies:
            enemy.update(self.enemies)

        for enemy_2 in self.enemies_2:
            enemy_2.update(self.enemies_2)

        for meteor in self.meteors:
            meteor.update(self.meteors)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

        for enemy_2 in self.enemies_2:
            enemy_2.draw(screen)

        for meteor in self.meteors:
            meteor.draw(screen)

