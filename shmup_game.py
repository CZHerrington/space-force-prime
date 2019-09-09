import pygame
import random
# from os import path


# define screen and refresh rate
WIDTH = 720
HEIGHT = 720
FPS = 30

# define colors'
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (165, 42, 42)
WHITE = (255, 255, 255)

# initial pygame and create game window
pygame.init()
# pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface(screen.get_size())
pygame.display.set_caption('Space Force Prime')
clock = pygame.time.Clock()



def newnpc():
    n = [Npc(), Friendly()]
    newn = random.choice(n)
    all_sprites.add(newn)
    npcs.add(newn)

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
        self.image = pygame.Surface((50, 50))
        self.image.fill((BLUE))
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 30
        self.speedx = 0
        self.speedy = 0
        
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
        projectiles.add(package)


# general class for all npc's
class Npc(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((RED))
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
        self.image.fill((YELLOW))
        


# projectile class for packages and weapons
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface((10, 30))
        self.image.fill((GREEN))
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
        self.image = pygame.Surface((20, 10))
        self.image.fill((BROWN))
    #     self.rect.bottom = y
    #     self.rect.centerx = x
    #     self.speedy = -5
    # def update(self):
    #     # self.rect.y += self.speedy
    #     self.rect.move_ip(0, self.speedy)
    #     if self.rect.bottom < 0:
    #         self.kill()

# create sprites and sprite groups
all_sprites = pygame.sprite.Group()
stars = pygame.sprite.Group()
npcs = pygame.sprite.Group()
projectiles = pygame.sprite.Group()

# Game initialization
# Generate random stars
generate_stars(4, 1, 100)
generate_stars(6, 2, 10)
generate_stars(8, 3, 5)

player = Player()
all_sprites.add(player)
for i in range(10):
    newnpc()

# game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
            if event.key == pygame.K_z:
                player.shoot_package()

    # update sprites
    all_sprites.update()

    # check projectile collision with npc
    hits = pygame.sprite.groupcollide(npcs, projectiles, True, True)
    for hit in hits:
        newnpc()

    # check npc collisions with player
    playerhits = pygame.sprite.spritecollide(player, npcs, False)
    if playerhits:
        running = False

    # Draw / render screen
    screen.fill(BLACK)

    # add stars
    for star in stars:
        star.update()
        star.display(screen)

    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()