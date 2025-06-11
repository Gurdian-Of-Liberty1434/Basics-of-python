#This activity, "Colorful Bounce," involves a moving rectangle (sprite) that bounces off the window edges. Each bounce changes its color and the window's background color, creating a dynamic display of colors

import pygame
import random

pygame.init()

SPRITE_COLOR_CHANGE_EVENT=pygame.USEREVENT+1
BACKGROUND_COLOR_CHANGE_EVENT=pygame.USEREVENT+2

BLUE=pygame.Color('blue')
LIGHT_BLUE=pygame.Color('lightblue')
DARK_BLUE=pygame.Color('darkblue')

YELLOW=pygame.Color('yellow')
MAGENTA=pygame.Color('magneta')
ORANGE=pygame.Color('orange')
WHITE=pygame.Color('white')

class Sprite(pygame.sprite.Sprite):
    def __init__(self, width, height, Color):
        super().__init__()
        self.image=pygame.surface([width, height])
        self.image.fill(Color)
        self.rect=self.image.get_rect()
        self.velocity=[random.choice([-1,1]),random.choice([-1,1])]

    def update(self, boundry_hit):
        self.rect.move_ip(self.velocity)
        boundry_hit=False
        if self.rect.left<=0 or self.rect.bottom>=400:
            self.velocity[0]*=-self.velocity[0]
            boundry_hit=True
        if self.rect.right>=400 or self.rect.top<=0:
            self.velocity[1]*=-self.velocity[1]
            boundry_hit=True
        if boundry_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))
    
    def change_color(self):
        self.image.fill(random.choice([YELLOW,MAGENTA,ORANGE,WHITE]))
def change_background(self):
    global bgcolor
    bgcolor=random.choice([BLUE,LIGHT_BLUE,DARK_BLUE])
    
all_sprites_list=pygame.sprite.Group()
sp1=Sprite(WHITE,20,30)

sp1.rect.x=random.randint(0,480)
sp1.rect.y=random.randint(0,400)

all_sprites_list.add(sp1)

screen=pygame.display.set_mode([500,400])
pygame.display.set_caption("Colorful Bounce")

bgcolor=BLUE
screen.fill(bgcolor)

clock=pygame.time.Clock()

while not exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=True
        elif event.type==SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type==BACKGROUND_COLOR_CHANGE_EVENT:
            change_background()
            