import pygame
# import random
# import text_scroll

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

# define runtime settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface(screen.get_size())
pygame.display.set_caption('Space Force Prime')
clock = pygame.time.Clock()