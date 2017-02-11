
def TitleScreen(screen):
    lul = pygame.image.load("TitleScreen/escape.png")
    screen.blit(lul, (0,0,1280,720))
    lul = pygame.image.load("TitleScreen/escapefilter.png")
    screen.blit(lul, (0,0,1280,720))
    lul = pygame.image.load("TitleScreen/FillerRussian.png")
    screen.blit(lul, (0,screen.get_height()/3,1280,720))#FILLer

    done = False
    clock = pygame.time.Clock()
    font25 = pygame.font.SysFont('Roboto Slab', 25, True, False)
    font40 = pygame.font.SysFont('Roboto Slab', 40, True, False)
    font120 = pygame.font.SysFont('Roboto Slab', 120, True, False)
    '''pygame.mixer.music.load("../Sound/Music/Tema.ogg")
    pygame.mixer.music.play(-1)'''
    Sound.soundlib.play_music("Tema.ogg", -1)
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
                #if pressed space
                if event.key == pygame.K_SPACE:
                    SPACE = True
                if event.key == pygame.K_RETURN:
                    SPACE = True
                #Move keys
                elif event.key == pygame.K_RIGHT:
                    RIGHT = True
                elif event.key == pygame.K_LEFT:
                    LEFT = True
                elif event.key == pygame.K_DOWN:
                    DOWN = True
                elif event.key == pygame.K_UP:
                    UP = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                MOUSE = True

        # --- Drawing code should go here
        butrects = [(600, h/2, 400, 50), (600, h/2+90, 400, 50), (600, h/2+180, 400, 50)]
        screen.fill((20,22,20), butrects[0])
        but1text = font25.render("Start", 2, sovietred)
        screen.blit(but1text, (700, h/2+6)) 
        screen.fill((20,22,20), butrects[1])
        but2text = font25.render("Settings", 2, sovietred)
        screen.blit(but2text, (700, h/2+96))
        screen.fill((20,22,20), butrects[2])
        but3text = font25.render("Exit", 2, sovietred)
        screen.blit(but3text, (700, h/2+186))
        title = font40.render("I don't know who, where or what I am doing, but I know I need to ", 2, sovietred)
        title2 = font120.render("Pobeg!", 2, sovietgold)
        screen.fill((20,22,20), (10,h/8,1260,60))
        screen.blit(title, (20, h/8)) 
        screen.fill((20,22,20), (w/3 *2 -30,h/4,400,140))
        screen.blit(title2, (w/3 *2 -20, h/4-20)) 
        
        if pygame.Rect(butrects[0]).collidepoint(mousex, mousey):
            return "start"
        elif pygame.Rect(butrects[1]).collidepoint(mousex, mousey):
            pass
        elif pygame.Rect(butrects[2]).collidepoint(mousex, mousey):
            return "exit"
        
        
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


if __name__ == "__main__":
    import pygame
    import Sound.soundlib
    pygame.init()
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    TitleScreen(screen)
    
