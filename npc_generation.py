import pygame
import random
from settings import *
from sprites import *

# difficulty curve > 0.5 = less enemies
# difficulty curve < 0.5 = less freindlies
# asteroid_num = 0
score = 0
difficulty_curve = max(0.7 - score/10, .1)
# methods for generating npcs
def new_npc():
    n = random.random()
    if n > difficulty_curve:
        new_enemy()
    elif n < difficulty_curve and n > difficulty_curve /2:
        new_friendly()
    elif n < difficulty_curve / 2:
        new_asteroid()

def new_asteroid():
    asteroid = Asteroid()
    all_sprites.add(asteroid)
    asteroids.add(asteroid)
    npcs.add(asteroid)

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
        self.rect.y = -250
        self.rect.bottom = -20
        self.speedy = random.randrange(4, 8)
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
        self.speedy = random.randrange(2, 5)
        self.speedx = random.randrange(-2, 2)

class Asteroid(Npc):
    def __init__(self):
        super().__init__()
        n = random.randint(0,2)
        asteroids = [asteroid1_img, asteroid2_img, asteroid3_img]
        self.image = pygame.transform.scale(asteroids[n], (50, 50))

    def update(self):
        # self.rect.x += self.speedx
        # self.rect.y += self.speedy
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.top > HEIGHT or self.rect.left < -50 or self.rect.right > WIDTH + 50:
            self.kill()
            new_npc()