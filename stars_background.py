import pygame
import random
from settings import *
from sprites import *
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