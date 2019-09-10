import pygame
from os import path

pygame.mixer.init()

snd_dir = path.join(path.dirname(__file__), 'sounds')
shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'shoot_weapon.wav'))
shoot_package_sound = pygame.mixer.Sound(path.join(snd_dir, 'send_package.wav'))

pygame.mixer.music.load(path.join(snd_dir, 'bground_loop.wav'))

pygame.mixer.music.play(loops = -1)