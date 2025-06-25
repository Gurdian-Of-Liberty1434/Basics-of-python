#Write a program where a player controls a sprite when two sprites collide , the game displaying a win message upon meeting a specific condition.
import pygame
import random

SCRREEN_WIDTH, SCREEN_HEIGHT = 500, 400

pygame.init()

background_image=pygame.transform.scale(pygame.image.load("landscape.jpg"),(SCRREEN_WIDTH,SCREEN_HEIGHT))

font=pygame.font.Font("Times New Roman",32)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image=pygame.surface([width, height])
        self.image.fill(pygame.Color('Dodgerblue'))
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))

    def move(self,x_change,y_change):
        self.rect.x=max(min(self.rect.x+x_change,SCRREEN_WIDTH-self.rect.width),0)
        self.rect.y=max(min(self.rect.y+y_change,SCREEN_HEIGHT-self.rect.height),0)

screen=pygame.display.set_mode((SCRREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision")
all_sprites=pygame.sprite.Group()

sprite1=Sprite(pygame.Color("black"), 50, 50)
sprite1.rect.x,sprite1.rect.y=random.randint(
    0,SCRREEN_WIDTH-sprite1.rect.width),random.randint(0,SCREEN_HEIGHT-sprite1.rect.height)
all_sprites.add(sprite1)

sprite2=Sprite(pygame.Color("red"), 50, 50)
sprite2.rect.x,sprite2.rect.y=random.randint(
    0,SCRREEN_WIDTH-sprite2.rect.width),random.randint(0,SCREEN_HEIGHT-sprite2.rect.height)
all_sprites.add(sprite2)

