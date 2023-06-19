import random
import pygame
from game.components.power_ups.heart import Heart
from game.components.power_ups.shield import Shield
from game.utils.constants import FONT_S, SCREEN_WIDTH, SPACESHIP, SPACESHIP_HEART_ARMOR, SPACESHIP_SHIELD

class PowerupsManager:
    def __init__(self):
        self.power_ups = []                           # Lista de power-ups presentes en el juego
        self.current_power_up = None                   # Power-up actual que está activo
        self.when_appears = random.randint(10000, 15000)  # Tiempo en milisegundos para la aparición del próximo power-up
        self.sound_powerup = pygame.mixer.Sound("game/assets/Sounds/power_up.ogg")  # Sonido de power-up adquirido
        self.generated_this_cycle = False              # Bandera para controlar la generación de power-ups en cada ciclo

    def generate_power_up(self):
        # Genera un nuevo power-up y lo agrega a la lista de power-ups
        power_up_types = [Shield, Heart]               # Lista de tipos de power-ups disponibles
        power_up_type = random.choice(power_up_types)  # Seleccionar un tipo de power-up al azar
        power_up = power_up_type()                     # Crear una instancia del power-up seleccionado
        self.power_ups.append(power_up)                # Agregar el power-up a la lista de power-ups
        self.current_power_up = power_up               # Establecer el power-up actual
        self.when_appears += random.randint(15000, 20000)  # Calcular el tiempo para la aparición del próximo power-up

    def update(self, game):
        # Actualiza el estado de los power-ups y verifica las colisiones con el jugador
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) == 0 and current_time >= self.when_appears and not self.generated_this_cycle:
            self.generate_power_up()
            self.generated_this_cycle = True

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if game.player.rect.colliderect(power_up):
                # El jugador ha colisionado con un power-up
                self.sound_powerup.play()
                if isinstance(power_up, Heart):
                    if not game.player.has_power_up:
                        # El jugador adquiere el power-up de corazón
                        game.player.has_power_up = True
                        game.player.power_up_type = power_up.type
                        game.player.set_image((80, 80), SPACESHIP_HEART_ARMOR)
                else:
                    if not game.player.has_power_up:
                        # El jugador adquiere el power-up de escudo
                        game.player.has_power_up = True
                        game.player.power_up_type = power_up.type
                        game.player.set_image((90, 90), SPACESHIP_SHIELD)

                self.power_ups.remove(power_up)
                self.current_power_up = None

        if len(self.power_ups) >= 1:
            # Desactivar el power-up actual si hay más de uno en la lista
            game.player.has_power_up = False
            game.player.set_image((70, 70), SPACESHIP)
            self.current_power_up = None

        if current_time > self.when_appears:
            self.generated_this_cycle = False

    def draw(self, screen):
        # Dibuja todos los power-ups en la pantalla
        for power_up in self.power_ups:
            power_up.draw(screen)

    def display_time_left(self, screen):
        # Muestra el tiempo restante para la aparición del próximo power-up en la pantalla
        current_time = pygame.time.get_ticks()
        time_left = max(0, self.when_appears - current_time)
        time_left_seconds = int(time_left / 1000)
        font = pygame.font.Font(FONT_S, 24)
        text = font.render(f"Next PowerUp: {time_left_seconds}s", True, (255, 255, 255))
        screen.blit(text, (10, 35))

    def reset(self, game):
        # Reinicia el administrador de power-ups
        self.power_ups = []
        self.current_power_up = None
        self.when_appears = random.randint(15000, 20000)
        self.generated_this_cycle = False
        # Restablecer el estado del jugador
        game.player.has_power_up = False
        game.player.set_image((70, 70), SPACESHIP)