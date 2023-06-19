import pygame
from pygame.sprite import Sprite
from game.components.bullets.bullet import Bullet
from game.utils.constants import DEFAULT_TYPE, PLAYER_TYPE, SCREEN_HEIGHT, SPACESHIP, SPACESHIP_DESTROY
from game.utils.constants import SCREEN_WIDTH


class Spaceship(Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (70, 70))
        self.destroyed_image = pygame.transform.scale(SPACESHIP_DESTROY, (60, 40))
        self.rect = self.image.get_rect()
        self.rect.x = 520
        self.rect.y = 500
        self.type = PLAYER_TYPE
        self.power_up_type = DEFAULT_TYPE
        self.has_power_up = False
        self.power_up_time = 0
        self.change_image_timer = 0
        self.sound = pygame.mixer.Sound("game/assets/Sounds/player_bullet.ogg")
        


    def update(self, user_input, bullet_manager):
        if user_input[pygame.K_LEFT]:
            self.move_left()
        elif user_input[pygame.K_RIGHT]:
            self.move_right()
        elif user_input[pygame.K_UP]:
            self.move_up()
        elif user_input[pygame.K_DOWN]:
            self.move_down()
        elif user_input[pygame.K_SPACE]:
            self.shoot(bullet_manager)
            self.sound.play()
            
            

    
    
    def move_left(self):
        self.rect.x -= 10
        if self.rect.left <= -50:
            self.rect.x = SCREEN_WIDTH

    def move_right(self):
        self.rect.x += 10
        if self.rect.right >= (SCREEN_WIDTH) + 50:
            self.rect.x = -50

    def move_up(self):
        if self.rect.y > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
         
    def move_down(self):
        if self.rect.y < SCREEN_HEIGHT - 50:
            self.rect.y += 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def shoot(self, bullet_manager):
        bullet = Bullet(self)
        bullet_manager.add_bullet(bullet)

    def set_image(self, size=(40,60), image=(SPACESHIP)):
        self.image = image
        self.image = pygame.transform.scale(self.image, size)



