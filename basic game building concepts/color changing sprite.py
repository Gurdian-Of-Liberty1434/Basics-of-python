#Write a program that detects when keys are pressed and changes the color of a sprite when it touches the screen boundaries
import pygame

def main():
    pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Color Changing Sprite")

    color={
        "red": pygame.Color('red'),
        "green": pygame.Color('green'),
        "blue": pygame.Color('blue'),
        "yellow": pygame.Color('yellow'),
        "white": pygame.Color('white')
    }
    current_color=color["white"]
    x, y=30,30
    sprite_width, sprite_height=30,30
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=True
        pressed=pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:x-=3
        if pressed[pygame.K_RIGHT]:x+=3
        if pressed[pygame.K_UP]:y-=3
        if pressed[pygame.K_DOWN]:y+=3
        
        x=min(max(x,0),screen_width-sprite_width)
        y=min(max(y,0),screen_height-sprite_height)
        