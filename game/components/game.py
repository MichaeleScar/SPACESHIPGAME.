import pygame
from game.components.bullets.bullet_manager import BulletManager
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_manager import EnemyManager
from game.components.menu import Menu
from game.components.death_menu import DeathMenu
from game.components.power_ups.powerups_manager import PowerupsManager


from game.components.spaceship import Spaceship

from game.utils.constants import BG, FINAL_TITLE_1, FONT_S, FONT_STYLE, GAMEOVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SPACESHIP_DESTROY, TITLE, FPS, DEFAULT_TYPE, TITLE_1, TITLE_2


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
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.enemy = Enemy()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu(ICON, TITLE_1, TITLE_2, "", text_size=40)
        self.death_menu = DeathMenu(SPACESHIP_DESTROY,GAMEOVER, FINAL_TITLE_1, "message 3")
        self.power_up_manager = PowerupsManager()
        
        
        
        self.lets_play = pygame.mixer.Sound("game/assets/Sounds/lets_play.ogg")
        
        self.menu_final = pygame.mixer.Sound("game/assets/Sounds/menu_final.ogg")

        self.intro_menu = pygame.mixer.Sound("game/assets/Sounds/intro_menu.ogg")
        
        self.intro_menu_played = False



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
        self.lets_play.play()

        while self.playing:
            self.events()
            self.update()
            self.draw()
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            
    
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager) 
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
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
        font = pygame.font.Font(FONT_S, 22)
        text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        
        if self.death_count > 0:
            self.menu_final.play() 
            self.death_menu.update_highest_score(self.score)
            self.highest_score = self.death_menu.highest_score
            self.death_menu.update_message(
                pygame.transform.scale(SPACESHIP_DESTROY, (50, 50)), 
                pygame.transform.scale(GAMEOVER, (300,100)),
                pygame.transform.scale(FINAL_TITLE_1, (500, 150)),
                f"HIGHEST SCORE: {self.highest_score}                SCORE: {self.score} DEATHS: {self.death_count}"
            )
            self.death_menu.draw(self.screen)
            self.menu.events(self.on_close, self.play)
        else:
            if not self.intro_menu_played:
                self.intro_menu.play()
                self.intro_menu_played = True
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
        self.power_up_manager.reset()
        self.menu_final.stop()
        self.intro_menu.stop()
        

    
