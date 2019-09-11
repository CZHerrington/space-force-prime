import pygame
from settings import *
from sprites import *
def show_start_screen():
    bg_rect = background.get_rect()
    screen.blit(background, bg_rect)
    # draw_text(screen, "Space Force Prime!", 64, WIDTH / 1.3, HEIGHT / 8)
    # draw_text(screen, "Arrow keys move, Space to fire", 22, WIDTH / 1.55, HEIGHT / 1.2)
    # draw_text(screen, "Press a key to begin", 22, WIDTH / 1.7, HEIGHT * 3.8 / 4)
    screen.blit(instructions1, (0, 0))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False
    screen.blit(instructions2, (0, 0))
    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                waiting = False