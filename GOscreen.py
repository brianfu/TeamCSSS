import Sound.soundlib
from time import sleep

def GO(pygame, screen):
    lul = pygame.image.load("TitleScreen/escape.png")
    screen.blit(lul, (0,0,1280,720))
    done = False
    clock = pygame.time.Clock()
    font120 = pygame.font.SysFont('TitleScreen/Imperial Web.ttf', 180)
    font10 = pygame.font.SysFont('TitleScreen/Imperial Web.ttf', 60)
    #Sound.soundlib.play_music("Tema.ogg", 1)
    sovietred = (204,0,0)
    sovietgold = (255,215,0)
    w,h = screen.get_width(), screen.get_height()
    mousex, mousey = 0,0
    # -------- Main Program Loop -----------
    while not done:
        SPACE = False
        RIGHT = False
        LEFT = False
        DOWN = False
        UP = False
        MOUSE = False
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #if event key down
            elif event.type == pygame.KEYDOWN:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

        # --- Drawing code should go here
        screen.fill((20,22,20))
        title2 = font120.render("GAME OVER, BRAT.", 2, sovietred)
        screen.blit(title2, (w/2 - title2.get_width()/2, h/4)) 
        title3 = font10.render("TRY AGAIN?", 2, sovietred)
        screen.blit(title3, (w/2 - title3.get_width()/2, h/2)) 
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        sleep(0.5)
        clock.tick(60)


if __name__ == "__main__":
    import pygame
    import Sound.soundlib
    pygame.init()
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    GO(pygame, screen)
    
