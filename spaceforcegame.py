import pygame
import random
import text_scroll
from sprites import *
from settings import *
from draw_methods import *
from npc_generation import *
from stars_background import *
from projectiles import *
from player import *
from start_screens import *

# initialize pygame and create game window
pygame.init()

pygame.mixer.init()

# game intro
text_scroll.intro()

player = Player()
score = 0

def game_over():
    screen.blit(game_over_img, (0, 0))
    draw_text(screen, 'SCORE: ' + str(score), 32, WIDTH - 70, 10)
    pygame.display.flip()
    wait = True
    while wait:
        pygame.time.delay(250)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   pygame.quit()
                elif event.key==pygame.K_RETURN:
                    player.reset()
                    for sprite in npcs:
                        sprite.kill()
                    for sprite in asteroids:
                        sprite.kill()
                    for i in range(10):
                        new_npc()
                    for i in range(5):
                        new_asteroid()
                    show_go_screen()
                    wait = False

pygame.mixer.music.play(loops = -1)
show_go_screen()

all_sprites.add(player)
for i in range(10):
    new_npc()
    
for i in range(5):
    new_asteroid()

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

    pygame.sprite.groupcollide(asteroids, projectiles, False, True)

    pygame.sprite.groupcollide(asteroids, packages, False, True)

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
            game_over()
            score = 0

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