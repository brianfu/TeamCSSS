import Sound.soundlib
from time import sleep

def WIN(pygame, screen):
    lul = pygame.image.load("TitleScreen/escape.png")
    screen.blit(lul, (0,0,1280,720))
    lul = pygame.image.load("TitleScreen/escapefilter.png")
    screen.blit(lul, (0,0,1280,720))
    done = False
    clock = pygame.time.Clock()
    font120 = pygame.font.SysFont('TitleScreen/Imperial Web.ttf', 180)
    font10 = pygame.font.SysFont('TitleScreen/Imperial Web.ttf', 60)
    #Sound.soundlib.play_music("Tema.ogg", 1)
    sovietred = (204,0,0)
    sovietgold = (255,215,0)
    Sound.soundlib.play_music("sun(titlescreen).mp3")
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
        title2 = font120.render("GAME WIN YOU!", 2, sovietgold)
        screen.blit(title2, (w/2 - title2.get_width()/2, h/4+h/8)) 
        title3 = font10.render("IN SOVIET RUSSIA", 2, (10,12,10))
        screen.blit(title3, (w/2 - title3.get_width()/2, h/4)) 
        title4 = font10.render("FROM THE TEAM, VERY VERY GRATZ!", 2, (10,12,10))
        screen.blit(title4, (w/2 - title4.get_width()/2, h/4*3)) 
        
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
    WIN(pygame, screen)
    
