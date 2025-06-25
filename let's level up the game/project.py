import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
YELLOW = (0, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 255)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def change_color(self, new_color):
        self.image.fill(new_color)

sprite1 = Sprite(100, 100, RED)
sprite2 = Sprite(300, 300, BLUE)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

CHANGE_COLOR = pygame.USEREVENT + 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == CHANGE_COLOR:
            sprite1.change_color(YELLOW)
            sprite2.change_color(GREEN)

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    pygame.time.set_timer(CHANGE_COLOR, 20)

    pygame.display.flip()

    pygame.time.Clock().tick(60)
