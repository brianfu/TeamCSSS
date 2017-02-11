
def TitleScreen(screen):
    screen.fill((204, 0, 0))
    done = False
    clock = pygame.time.Clock()
    pygame.mixer.music.load("../Music/sun(titlescreen).mp3")
    pygame.mixer.music.play(-1)
    # -------- Main Program Loop -----------
    while not done:
        SPACE = False
        RIGHT = False
        LEFT = False
        DOWN = False
        UP = False
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


        # --- Game logic should go here

       
        # --- Screen-clearing code goes here

        # Here, we clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.

        # If you want a background image, replace this clear with blit'ing the
        # background image.
        #screen.fill(WHITE)

        # --- Drawing code should go here
        font.render("I don't know who, where or what I am doing, but I know I need to Pobeg!", 

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)


if __name__ == "__main__":
    import pygame
    pygame.init()
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    TitleScreen(screen)
