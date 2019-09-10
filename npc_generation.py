import pygame
import random
from settings import *
from sprites import *

# difficulty curve > 0.5 = less enemies
# difficulty curve < 0.5 = less freindlies
difficulty_curve = 0.5
asteroid_num = 0

# init explosion animation
explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)

# methods for generating npcs
def new_npc():
    n = random.random()
    if n > difficulty_curve: new_enemy()
    else: new_friendly()

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
        self.speedy = random.randrange(1, 5)
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

class Asteroid(Npc):
    def __init__(self):
        super().__init__()
        n = random.randint(0,2)
        asteroids = [asteroid1_img, asteroid2_img, asteroid3_img]
        self.image = pygame.transform.scale(asteroids[n], (50, 50))

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

