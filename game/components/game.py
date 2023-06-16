import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.death_menu import DeathMenu


from game.components.spaceship import Spaceship

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.score = 0
        self.death_count = 0
        self.highest_score = 0 
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.enemy = Enemy()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu("SPACESHIP JOURNEY 16BITS", "PRESS ANY KEY TO START...", "")
        self.death_menu = DeathMenu("message", "message 2", "message 3")



    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.reset_all()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager) 
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        if self.death_count > 0:
            self.death_menu.update_highest_score(self.score)
            self.highest_score = self.death_menu.highest_score
        
            self.death_menu.update_message(f"HIGHEST SCORE: {self.highest_score}", f"SCORE: {self.score}", f"DEATHS: {self.death_count}")
            
            self.death_menu.draw(self.screen)
            self.menu.events(self.on_close, self.play)
        else:
            self.menu.draw(self.screen)
            self.menu.events(self.on_close, self.play)

    def on_close(self):
        self.playing = False
        self.running = False
    
    def reset_all(self):
        self.bullet_manager.reset()
        self.enemy_manager.reset()
        self.playing = True
        self.score = 0
