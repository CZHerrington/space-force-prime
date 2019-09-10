import pygame
from settings import *
from sprites import *
from projectiles import *

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