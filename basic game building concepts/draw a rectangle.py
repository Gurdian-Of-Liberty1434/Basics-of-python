import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen, (0,125,255), pygame.Rect(30,50,60,100))
    pygame.display.flip()