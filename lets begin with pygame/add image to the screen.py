import pygame

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Adding image and background")

background = pygame.transform.scale(
    pygame.image.load('mountfuji.jpeg').convert()
    ,(SCREEN_WIDTH, SCREEN_HEIGHT))

tower = pygame.transform.scale(
    pygame.image.load("paris-tower-removebg-preview.png").convert_alpha(),(200,200))
tower_rect=tower.get_rect(center=(SCREEN_HEIGHT//2
                                  ,SCREEN_WIDTH//2-30))

text=pygame.font.Font(None,36).render("Hello world",True,
                                      pygame.color("black"))
text_rect=text.get_rect(center=(SCREEN_HEIGHT//2,
                                SCREEN_WIDTH//2+110))

def game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(background,(0,0))
        display_surface.blit(tower,tower_rect)
        display_surface.blit(text,text_rect)
        pygame.display.flip()
        clock.tick(30)

pygame.quit()

if __name__ == "__main__":
    game_loop()


