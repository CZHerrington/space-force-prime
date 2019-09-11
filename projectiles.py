import pygame
from settings import *
from sprites import *
# projectile class for packages and weapons
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -12

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
        self.speedy = -12
    # def update(self):
    #     # self.rect.y += self.speedy
    #     self.rect.move_ip(0, self.speedy)
    #     if self.rect.bottom < 0:
    #         self.kill()