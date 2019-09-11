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
from sounds import *
from explosions import *

# initialize pygame and create game window
pygame.init()

pygame.mixer.init()

# game intro
text_scroll.intro()

player = Player()


def game_over():
    enemy_count = 15
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
                    for sprite in explosions:
                        sprite.kill()
                    for sprite in projectiles:
                        sprite.kill()
                    for sprite in packages:
                        sprite.kill()
                    for sprite in npcs:
                        sprite.kill()
                    for sprite in asteroids:
                        sprite.kill()
                    show_start_screen()
                    wait = False

pygame.mixer.music.play(loops = -1)
pygame.mixer.music.set_volume(0.6)

show_start_screen()

all_sprites.add(player)
# for i in range(15):
#     new_npc()

# game loop
enemy_count = 15
last_spawn = 0
spawn_delay = 0
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    now = pygame.time.get_ticks()
    if (now - spawn_delay) >= last_spawn and enemy_count > 0:
        new_npc()
        spawn_delay = random.randint(0, 3000)
        enemy_count -= 1
        last_spawn = now
    # staggered spawn

    # update sprites
    all_sprites.update()

    # check projectile collision with npcs
    enemy_hits = pygame.sprite.groupcollide(enemies, projectiles, True, True)
    for hit in enemy_hits:
        weapon_hit_sound.play()
        exp = Explosion(hit.rect.center, 'lg')
        all_sprites.add(exp)
        explosions.add(exp)
        score += 1
        new_npc()

    friendly_hits = pygame.sprite.groupcollide(deliveries, projectiles, True, True)
    for hit in friendly_hits:
        exp = Explosion(hit.rect.center, 'lg')
        all_sprites.add(exp)
        explosions.add(exp)
        score -= 1
        weapon_hit_sound.play()
        new_npc()

    asteroid_hits = pygame.sprite.groupcollide(asteroids, projectiles, False, True)
    for hit in asteroid_hits:
        exp = Explosion(hit.rect.center, 'sm')
        all_sprites.add(exp)
        explosions.add(exp)
        weapon_hit_sound.play()

    pygame.sprite.groupcollide(asteroids, packages, False, True)

    enemy_package_hits = pygame.sprite.groupcollide(enemies, packages, True, True)
    for hit in enemy_package_hits:
        package_misdelivered_sound.play()
        score -= 1
        new_npc()

    friendly_package_hits = pygame.sprite.groupcollide(deliveries, packages, True, True)
    for hit in friendly_package_hits:
        score += 1
        exp = StarExplosion(hit.rect.center)
        all_sprites.add(exp)
        explosions.add(exp)
        package_delivered_sound.play()
        new_npc()

    # check npc collisions with player
    playerhits = pygame.sprite.spritecollide(player, npcs, True)
    if playerhits:
        asteroid_collision_sound.play()
        player.health -= 40
        new_npc()
        exp = Explosion(player.rect.center, 'laser')
        all_sprites.add(exp)
        explosions.add(exp)
        if player.health <= 0:
            enemy_count = 15
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