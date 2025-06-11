import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 640, 480
SPEED = 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

rect1 = pygame.Rect(100, 100, 50, 50)
rect2 = pygame.Rect(300, 300, 50, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        rect1.y -= SPEED
    if keys[pygame.K_DOWN]:
        rect1.y += SPEED
    if keys[pygame.K_LEFT]:
        rect1.x -= SPEED
    if keys[pygame.K_RIGHT]:
        rect1.x += SPEED

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)

    pygame.display.flip()

    pygame.time.Clock().tick(60)