import pygame
from game.utils.constants import BG, FONT_S, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, TITLE_1, TITLE_2

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, icon, message, message_2, message_3, text_size=30):
        self.font = pygame.font.Font(FONT_S, text_size)
        self.update_message(icon, message, message_2, message_3)
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0

    def events(self, on_close, on_start):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on_close()
            elif event.type == pygame.KEYDOWN:
                on_start()

    def draw(self, screen):
        screen.fill((255, 255, 250))
        self.draw_background()
        screen.blit(self.image, self.image_rect)
        screen.blit(self.icon, self.icon_rect)
        screen.blit(self.image_2, self.image_2_rect)
        screen.blit(self.text_3, self.text_3_rect)
        pygame.display.update()

    def update_message(self, icon, title_1, title_2, message_3):
        # Actualizar los mensajes
        self.icon = pygame.transform.scale(icon, (100, 100))
        self.image = pygame.transform.scale(title_1, (1000, 150))
        self.image_2 = pygame.transform.scale(title_2, (800, 150))
        self.message_3 = message_3

        # Icono
        self.icon_rect = self.icon.get_rect()
        self.icon_rect.center = (self.HALF_SCREEN_WIDTH - 5, self.HALF_SCREEN_HEIGHT)

        # Renderizar y posicionar el primer mensaje
        self.image_rect = self.image.get_rect()
        self.image_rect.centerx = self.HALF_SCREEN_WIDTH
        self.image_rect.y = self.HALF_SCREEN_HEIGHT - 230

        # Renderizar y posicionar el segundo mensaje
        self.image_2_rect = self.image_2.get_rect()
        self.image_2_rect.centerx = self.HALF_SCREEN_WIDTH
        self.image_2_rect.y = self.HALF_SCREEN_HEIGHT + 80

        # Renderizar y posicionar el tercer mensaje
        self.text_3 = self.font.render(self.message_3, True, (255, 255, 250))
        self.text_3_rect = self.text_3.get_rect()
        self.text_3_rect.centerx = self.HALF_SCREEN_WIDTH + 10
        self.text_3_rect.y = self.HALF_SCREEN_HEIGHT

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed
