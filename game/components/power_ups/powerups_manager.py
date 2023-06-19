
import random
import pygame
from game.components.power_ups.heart import Heart

from game.components.power_ups.shield import Shield
from game.utils.constants import SPACESHIP, SPACESHIP_HEART_ARMOR, SPACESHIP_SHIELD

class PowerupsManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(25000, 30000)
        self.duration = 1
        self.sound_powerup = pygame.mixer.Sound("game/assets/Sounds/power_up.ogg")
        



    def generate_power_up(self):
        power_up_types = [Heart, Heart]
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
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.power_up_type = power_up.type
                    game.player.power_up_time =  self.duration * 1000
                    game.player.set_image((80, 80), SPACESHIP_HEART_ARMOR)
                    self.power_ups.remove(power_up)
                else:
                    power_up.start_time = pygame.time.get_ticks()
                    game.player.has_power_up = True
                    game.player.power_up_type = power_up.type
                    game.player.power_up_time =  self.duration * 1000
                    game.player.set_image((90, 90), SPACESHIP_SHIELD)
                    self.power_ups.remove(power_up)
            if game.player.has_power_up and (current_time - power_up.start_time >= self.duration or not game.playing):
                game.player.has_power_up = False
                game.player.set_image((70, 70), SPACESHIP)
                
    
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)


    

    def reset(self):
         now = pygame.time.get_ticks()
         self.power_ups = []
         self.when_appears = now + self.duration + random.randint(10000, 15000)
         self.tart_time = 0
         
         

    


        
