import pygame
import random

from os import path
img_dir = path.join(path.dirname(__file__), 'img')

# define screen and refresh rate
WIDTH = 720
HEIGHT = 720
FPS = 30

# define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (165, 42, 42)
WHITE = (255, 255, 255)

# initialize pygame and create game window
pygame.init()

# pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface(screen.get_size())
pygame.display.set_caption('Space Force Prime')
clock = pygame.time.Clock()

#define resources
bullet_img = pygame.image.load(path.join(img_dir, "bullet_short_single.png"))
player_img = pygame.image.load(path.join(img_dir, 'WO84-wu-X3.png'))
npc_img = pygame.image.load(path.join(img_dir, 'CX16-X3.png'))
friendly_img = pygame.image.load(path.join(img_dir, 'DKO-api-X3.png'))
logo_img = pygame.image.load(path.join(img_dir, 'spaceforcelogo.png'))
package_img = pygame.image.load(path.join(img_dir, 'package.png'))


def new_npc():
    n = random.random()
    if n > 0.5: new_enemy()
    else: new_friendly()

def new_friendly():
    nnpc = Friendly()
    all_sprites.add(nnpc)
    npcs.add(nnpc)
    deliveries.add(nnpc)

def new_enemy():
    nnpc = Npc()
    all_sprites.add(nnpc)
    npcs.add(nnpc)
    enemies.add(nnpc)

def show_go_screen():
    bg_rect = background.get_rect()
    screen.blit(background, bg_rect)
    draw_text(screen, "Space Force Prime!", 64, WIDTH / 1.3, HEIGHT / 8)
    draw_text(screen, "Arrow keys move, Space to fire", 22, WIDTH / 1.55, HEIGHT / 1.2)
    draw_text(screen, "Press a key to begin", 22, WIDTH / 1.7, HEIGHT * 3.8 / 4)
    logo_img_scaled = pygame.transform.scale(logo_img, (int(694 / 2), int(864 / 2)))
    screen.blit(logo_img_scaled, (150, 150))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def draw_health_bar(surf, x, y, remaining_health):
    if remaining_health < 0:
        remaining_health = 0
    bar_length = 150
    bar_height = 15
    filled_bar = remaining_health * bar_length / 100
    outline_rect = pygame.Rect(x, y, bar_length, bar_height)
    fill_rect = pygame.Rect(x, y, filled_bar, bar_height)
    pygame.draw.rect(surf, RED, outline_rect)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def draw_text(surf, text, size, x, y):
    font = pygame.font.SysFont('arial', size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

# generate random star
def generate_stars(speed, radius, num):
    for i in range(num):
        w = random.randrange(0, WIDTH)
        h = random.randrange(0, HEIGHT)
        stars.add(Star(w, h, speed, radius))

class Star(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, radius):
        pygame.sprite.Sprite.__init__(Star, self)
        self.x = x
        self.y = y
        self.speed = speed
        self.radius = radius

    def update(self):
        self.y += self.speed
        if self.x > WIDTH:
            self.x = 0
        if self.y > HEIGHT:
            self.y = 0

    def display(self, screen):
        pygame.draw.circle(screen, WHITE, (self.x, self.y), self.radius)

# class for ship controlled by player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill((BLUE))
        self.image = pygame.transform.scale(player_img, (64, 56))
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 30
        self.speedx = 0
        self.speedy = 0
        self.health = 100
        
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -10
        if keystate[pygame.K_RIGHT]:
            self.speedx = 10
        if keystate[pygame.K_UP]:
            self.speedy = -10
        if keystate[pygame.K_DOWN]:
            self.speedy = 10
        # self.rect.x += self.speedx
        # self.rect.y += self.speedy
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        projectile = Projectile(self.rect.centerx, self.rect.top)
        all_sprites.add(projectile)
        projectiles.add(projectile)

    def shoot_package(self):
        package = Package(self.rect.centerx, self.rect.top)
        all_sprites.add(package)
        packages.add(package)


# general class for all npc's
class Npc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill((RED))
        self.image = pygame.transform.scale(npc_img, (50, 50))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()

        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = -50
        self.rect.bottom = -20
        self.speedy = 2
        self.speedx = random.randrange(-2, 2)
        

    def update(self):
        # self.rect.x += self.speedx
        # self.rect.y += self.speedy
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.top > HEIGHT or self.rect.left < -50 or self.rect.right > WIDTH + 50:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = -50


class Friendly(Npc):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(friendly_img, (50, 50))
        self.image = pygame.transform.rotate(self.image, 180)
        


# projectile class for packages and weapons
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -5

    def update(self):
        # self.rect.y += self.speedy
        self.rect.move_ip(0, self.speedy)
        if self.rect.bottom < 0:
            self.kill()

class Package(Projectile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.transform.scale(package_img, (30, 30))
        # self.image = pygame.Surface((20, 10))
        # self.image.fill((BROWN))
    #     self.rect.bottom = y
    #     self.rect.centerx = x
    #     self.speedy = -5
    # def update(self):
    #     # self.rect.y += self.speedy
    #     self.rect.move_ip(0, self.speedy)
    #     if self.rect.bottom < 0:
    #         self.kill()
# Load images


# create sprites and sprite groups
all_sprites = pygame.sprite.Group()
stars = pygame.sprite.Group()
npcs = pygame.sprite.Group()
deliveries = pygame.sprite.Group()
enemies = pygame.sprite.Group()

projectiles = pygame.sprite.Group()
packages = pygame.sprite.Group()

# Game initialization
show_go_screen()

# Generate random stars
generate_stars(4, 1, 100)
generate_stars(6, 2, 10)
generate_stars(8, 3, 5)

player = Player()
all_sprites.add(player)
for i in range(10):
    new_npc()

score = 0
# game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.shoot()
            if event.key == pygame.K_a:
                player.shoot_package()

    # update sprites
    all_sprites.update()

    # check projectile collision with npcs
    enemy_hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
    for hit in enemy_hits:
        score += 1
        new_npc()

    friendly_hits = pygame.sprite.groupcollide(deliveries, projectiles, True, True)
    for hit in friendly_hits:
        score -= 1
        new_npc()

    enemy_package_hits = pygame.sprite.groupcollide(enemies, packages, True, True)
    for hit in enemy_package_hits:
        score -= 1
        new_npc()

    friendly_package_hits = pygame.sprite.groupcollide(deliveries, packages, True, True)
    for hit in friendly_package_hits:
        score += 1
        new_npc()

    # check npc collisions with player
    playerhits = pygame.sprite.spritecollide(player, npcs, True)
    if playerhits:
        player.health -= 40
        new_npc()
        if player.health <= 0:
            running = False

    # Draw / render screen
    screen.fill(BLACK)

    # add stars
    for star in stars:
        star.update()
        star.display(screen)

    all_sprites.draw(screen)
    draw_health_bar(screen, 10, 10, player.health)
    draw_text(screen, 'SCORE: ' + str(score), 32, WIDTH - 70, 10)
    pygame.display.flip()

pygame.quit()