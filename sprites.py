import pygame
from os import path

img_dir = path.join(path.dirname(__file__), 'img')

#define resources
bullet_img = pygame.image.load(path.join(img_dir, "bullet_short_single.png"))
player_img = pygame.image.load(path.join(img_dir, 'WO84-wu-X3.png'))
npc_img = pygame.image.load(path.join(img_dir, 'CX16-X3.png'))
friendly_img = pygame.image.load(path.join(img_dir, 'DKO-api-X3.png'))
logo_img = pygame.image.load(path.join(img_dir, 'spaceforcelogo.png'))
package_img = pygame.image.load(path.join(img_dir, 'package.png'))
asteroid1_img = pygame.image.load(path.join(img_dir, 'asteroid1.png'))
asteroid2_img = pygame.image.load(path.join(img_dir, 'asteroid2.png'))
asteroid3_img = pygame.image.load(path.join(img_dir, 'asteroid3.png'))
instructions1 = pygame.image.load(path.join(img_dir, 'go_screen.png'))
instructions2 = pygame.image.load(path.join(img_dir, 'howtoplay.png'))
game_over_img = pygame.image.load(path.join(img_dir, 'game_over.png'))

# create sprites and sprite groups
all_sprites = pygame.sprite.Group()
stars = pygame.sprite.Group()
npcs = pygame.sprite.Group()
deliveries = pygame.sprite.Group()
enemies = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

projectiles = pygame.sprite.Group()
packages = pygame.sprite.Group()

explosions = pygame.sprite.Group()