import pygame
import random
from settings import *

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