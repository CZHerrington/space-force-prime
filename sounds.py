import pygame
from os import path

pygame.mixer.init()

snd_dir = path.join(path.dirname(__file__), 'sounds')
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'shoot_weapon.wav'))
shoot_package_sound = pygame.mixer.Sound(path.join(snd_dir, 'send_package.wav'))
package_delivered_sound = pygame.mixer.Sound(path.join(snd_dir, "package_delivered.wav"))
weapon_hit_sound = pygame.mixer.Sound(path.join(snd_dir, "weapon_hit.aiff"))
package_misdelivered_sound = pygame.mixer.Sound(path.join(snd_dir, "package_misdelivered.wav"))
asteroid_collision_sound = pygame.mixer.Sound(path.join(snd_dir, "asteroid_collision.ogg"))

pygame.mixer.music.load(path.join(snd_dir, 'bground_loop.wav'))

pygame.mixer.music.play(loops = -1)