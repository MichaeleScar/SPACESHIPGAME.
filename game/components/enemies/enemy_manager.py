from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2
from game.components.enemies.meteor import Meteor

class EnemyManager:
    def __init__(self):
        self.enemies: list[Enemy] = []
        self.enemies_2: list[Enemy_2] = []
        self.meteors: list[Meteor] = []

    def update(self):
        if not self.enemies:
            self.enemies.append(Enemy())
        if not self.enemies_2:
            self.enemies_2.append(Enemy_2())
        if not self.meteors:
            self.meteors.append(Meteor())

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
