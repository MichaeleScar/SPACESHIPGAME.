import random
import pygame
from game.components.power_ups.heart import Heart
from game.components.power_ups.shield import Shield
from game.utils.constants import FONT_S, SCREEN_WIDTH, SPACESHIP, SPACESHIP_HEART_ARMOR, SPACESHIP_SHIELD

class PowerupsManager:

    def __init__(self):
        self.power_ups = []
        self.current_power_up = None
        self.when_appears = random.randint(10000, 15000)
        self.sound_powerup = pygame.mixer.Sound("game/assets/Sounds/power_up.ogg")
        self.generated_this_cycle = False

    def generate_power_up(self):
        power_up_types = [Shield, Heart]
        power_up_type = random.choice(power_up_types)
        power_up = power_up_type()
        self.power_ups.append(power_up)
        self.current_power_up = power_up
        self.when_appears += random.randint(15000, 20000)

    def update(self, game):
        current_time = pygame.time.get_ticks()
        if len(self.power_ups) == 0 and current_time >= self.when_appears and not self.generated_this_cycle:
            self.generate_power_up()
            self.generated_this_cycle = True

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                self.sound_powerup.play()
                if isinstance(power_up, Heart):
                    if not game.player.has_power_up:
                        game.player.has_power_up = True
                        game.player.power_up_type = power_up.type
                        game.player.set_image((80, 80), SPACESHIP_HEART_ARMOR)
                else:
                    if not game.player.has_power_up:
                        game.player.has_power_up = True
                        game.player.power_up_type = power_up.type
                        game.player.set_image((90, 90), SPACESHIP_SHIELD)
                self.power_ups.remove(power_up)
                self.current_power_up = None

        if len(self.power_ups) >= 1:  # Desactivar el power-up actual si hay más de uno en la lista
            game.player.has_power_up = False
            game.player.set_image((70, 70), SPACESHIP)
            self.current_power_up = None

        if current_time > self.when_appears:
            self.generated_this_cycle = False

    def reset(self, game):
        self.power_ups = []
        self.current_power_up = None
        self.when_appears = random.randint(15000, 20000)
        self.generated_this_cycle = False

        # Restablecer el estado del jugador
        game.player.has_power_up = False
        game.player.set_image((70, 70), SPACESHIP)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def display_time_left(self, screen):
        current_time = pygame.time.get_ticks()
        time_left = max(0, self.when_appears - current_time)
        time_left_seconds = int(time_left / 1000)  # Convertir a segundos
        font = pygame.font.Font(FONT_S, 24)
        text = font.render(f"Next PowerUp: {time_left_seconds}s", True, (255, 255, 255))
        
        screen.blit(text, (10, 35))
