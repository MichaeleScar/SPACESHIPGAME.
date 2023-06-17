
import random
import pygame

from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP_SHIELD

class PowerupsManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(10000, 15000)
        self.duration = random.randint(2000, 5000)
        self.power_up_start_time = 0
        


    def generate_power_up(self):
        shield = Shield()
        self.power_ups.append(shield)
        self.when_appears += random.randint(10000, 15000)
        

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time  >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                game.player.has_power_up = True
                self.power_up_start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.power_up_time = self.power_up_start_time
                game.player.set_image((65, 85), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)
            if game.player.has_power_up and current_time - self.power_up_start_time >= self.duration:
                game.player.has_power_up = False
                
                
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(now + 10000, now + 15000)
        self.power_up_start_time = 0

    


        
