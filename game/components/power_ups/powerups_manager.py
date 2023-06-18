
import random
import pygame
from game.components.power_ups.heart import Heart

from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP, SPACESHIP_SHIELD

class PowerupsManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(10000, 15000)
        self.duration = 10000
        self.power_up_start_time = 0
        self.sound_powerup = pygame.mixer.Sound("game/assets/Sounds/power_up.ogg")
        



    def generate_power_up(self):
        power_up_types = [Shield, Heart]
        power_up_type = random.choice(power_up_types)
        power_up = power_up_type()
        self.power_ups.append(power_up)
        self.when_appears += random.randint(25000, 30000)
        


        

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appears:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                self.sound_powerup.play()
                if type(power_up) == Heart:
                    game.player.health += 1
                else:
                    game.player.has_power_up = True
                    self.power_up_start_time = pygame.time.get_ticks()
                    game.player.power_up_type = power_up.type
                    game.player.power_up_time = self.power_up_start_time
                    game.player.set_image((65, 85), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
            if game.player.has_power_up and current_time - self.power_up_start_time >= self.duration:
                game.player.has_power_up = False
                game.player.set_image((60, 40), SPACESHIP)
                
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        now = pygame.time.get_ticks()
        self.power_ups = []
        self.when_appears = random.randint(now + 10000, now + 15000)
        self.power_up_start_time = 0

    


        
