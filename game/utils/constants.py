import pygame
import os
pygame.init()

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

# Define the desired new size
new_width = 50  # Insert the desired width in pixels
new_height = 50  # Insert the desired height in pixels

# Resize the image
HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/heart_armor.png'))
HEART = pygame.transform.scale(HEART, (new_width, new_height))



DEFAULT_TYPE = "default"
SHIELD_TYPE = 'shield'
HEART_TYPE = 'heart'
ENEMY_TYPE = 'enemy'
PLAYER_TYPE = 'player_1'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
SPACESHIP_HEART_ARMOR = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_heart_armor.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))
SPACESHIP_DESTROY = pygame.image.load(os.path.join(IMG_DIR, "Destroy/spaceship_destroy.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMY_1 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png"))
ENEMY_2 = pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png"))
METEOR_1 = pygame.image.load(os.path.join(IMG_DIR, "Environment/meteor.png"))
METEOR_DESTROY = pygame.image.load(os.path.join(IMG_DIR, "Destroy/meteor_destroy.png"))
ENEMY_DESTROY = pygame.image.load(os.path.join(IMG_DIR, "Destroy/enemy_destroy.png"))

FONT_S = "game/assets/Fonts/ka1.ttf"
FONT_STYLE = 'freesansbold.ttf'

TITLE_1 = pygame.image.load(os.path.join(IMG_DIR, "Menus/menu_title_1.png"))
TITLE_2 = pygame.image.load(os.path.join(IMG_DIR, "Menus/menu_title_2.png"))
GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, "Menus/game_over.png"))
FINAL_TITLE_1 = pygame.image.load(os.path.join(IMG_DIR, "Menus/final_menu_1.png"))
