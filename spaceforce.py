import pygame
import random

# declare constants
FPS = 60
WIDTH = 1000
HEIGHT = 1000
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background = pygame.Surface(screen.get_size())
clock = pygame.time.Clock()
pygame.display.set_caption('Star Example')

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

all_sprites = pygame.sprite.Group()
star_list = pygame.sprite.Group()

def main():
    # generate random star
    def generate_stars(speed, radius, num):
        for i in range(num):
            w = random.randrange(0, WIDTH)
            h = random.randrange(0, HEIGHT)
            star_list.add(Star(w, h, speed, radius))

    # Game initialization
    # Generate random stars
    generate_stars(4, 1, 100)
    generate_stars(6, 2, 10)
    generate_stars(8, 3, 5)
    
    stop_game = False
    while not stop_game:
        clock.tick(FPS)
        for event in pygame.event.get():
            # Event handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                print('mouse down at %d, %d' % event.pos)
            if event.type == pygame.MOUSEBUTTONUP:
                print('mouse up at %d, %d' % event.pos)
            if event.type == pygame.KEYUP:
                print('key up %r' % event.key)
            if event.type == pygame.KEYDOWN:
                print('key down %r' % event.key)
            if event.type == pygame.QUIT:
                stop_game = True
                # if they closed the window, set stop_game to True
                # to exit the main loop
                stop_game = True

        # Game logic

        # Draw background !THIS HAS TO BE DRAWN FIRST AS IT IS THE BACKGROUND!
        background.fill(BLACK)
        screen.blit(background, (0, 0))
        for star in star_list:
            star.update()
            star.display(screen)
        
        # draw non-background sprites:


        # display next frame
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
