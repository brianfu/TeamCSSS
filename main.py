import os, sys
import pygame
from pygame.locals import *
import Core.load_sound
import Core.load_image
from Core.detect_collision import detect_collision
import Core.Command
import Char.Character
import Char.Enemy
import Core.Level
import Core.Bullet
import Core.Cursor
import TitleScreen
import Sound.soundlib
import Sound.charsoundhandler
import GOscreen
import WINscreen
import Core.draw_tile
import Core.textboxthatworks
import Core.Cursor

if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (204, 0, 0)
YELLOW = (255, 215, 0)
GREY = (100,100,100)
NAVY_BLUE = (25,25,112)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("No Swears Pls - Das Spiel")

font25 = pygame.font.SysFont('Calibri', 25, True, False)

# Start Title Menu
if not TitleScreen.TitleScreen(pygame, screen):
    done = True
    pygame.quit()
    sys.exit()

pygame.mouse.set_visible(False)

# Loop until the user clicks the close button.
done = False

gameOver = False
gameWin = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Define
keys_pressed = []


## CHANGE THIS BECAUSE IT IS ARCHAIC ##
Chardude = Char.Character.Character();
#group = pygame.sprite.Group(Chardude)

Command = Core.Command.Command();
tick = 0;

oldbody = [Char.Enemy.Enemy(50,50)];
oldbody[0].images = [pygame.image.load('Art/Player_original_head.png'),pygame.image.load('Art/Arms.png')]
oldbody[0].hasGun = False
Chardude.absorb(oldbody,0);

current_level = Core.Level.Level()
current_level.load_level(1)
current_room = current_level.get_current_room()
current_entities = current_level.get_current_entities()
current_bullets = []; # List of bullets in a room, reset on room change
Chardude.Pos_x = current_level.start_position[0]
Chardude.Pos_y = current_level.start_position[1]

shooting = False
click = False
click_pos = [0,0]

#
enemyAlertness = 0.0

#Define textbox
textbox = Core.textboxthatworks.textbox(screen)

# Start the tunes
Sound.soundlib.play_music("Ambi.ogg", -1)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # Check for Action E
        elif event.type == KEYDOWN and event.key == K_e:
            keys_pressed.append(event.key);

            gridpos_x = int((Chardude.Pos_x+20)//30)
            gridpos_y = int((Chardude.Pos_y+20)//30)

            if (int(current_room[gridpos_x][gridpos_y]) == 9 and Chardude.Ghoststate==False):
                current_room[gridpos_x][gridpos_y] = 13
                current_level.activate_room_lever()
            elif ((gridpos_x+1) <= 35 and int(current_room[gridpos_x+1][gridpos_y]) == 9 and Chardude.Ghoststate==False):
                current_room[gridpos_x+1][gridpos_y] = 13
                current_level.activate_room_lever()
            elif ((gridpos_x-1) >= 0 and int(current_room[gridpos_x-1][gridpos_y]) == 9 and Chardude.Ghoststate==False):
                current_room[gridpos_x-1][gridpos_y] = 13
                current_level.activate_room_lever()
            elif ((gridpos_y+1) <= 23 and int(current_room[gridpos_x][gridpos_y+1]) == 9 and Chardude.Ghoststate==False):
                current_room[gridpos_x][gridpos_y+1] = 13
                current_level.activate_room_lever()
            elif ((gridpos_y-1) >= 0 and int(current_room[gridpos_x][gridpos_y-1]) == 9 and Chardude.Ghoststate==False):
                current_room[gridpos_x][gridpos_y-1] = 13
                current_level.activate_room_lever()

        #if event key down
        elif event.type == pygame.KEYDOWN:
            keys_pressed.append(event.key);
        elif event.type == pygame.KEYUP:
            keys_pressed.remove(event.key);
        if event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()
            if Chardude.hasGun:
                shooting = True
            click = True
        else:
            click = False
        Command.makeFromEvent(event);
        Chardude.getCommand(Command);
        textbox.txt_getcmd(Command)
        

    if shooting:
        current_bullets.append(Core.Bullet.Bullet(Chardude.Pos_x + Chardude.size[0]/2, Chardude.Pos_y + Chardude.size[1]/2, click_pos[0], click_pos[1], True))
        shooting = False

    # --- Game logic should go here
    current_tile = Chardude.getTile()
    ## CODE FOR MOVING ROOMS ##
    if (current_tile[0] % 35 == 0 or current_tile[1] % 23 == 0) and not Chardude.Ghoststate:
        current_level.enter_door(current_tile, Chardude)
        current_room = current_level.get_current_room()
        current_entities = current_level.get_current_entities()
        current_bullets.clear();
        current_entities = current_level.get_current_entities()
    ## CODE UPDATING ##
    for enemy in current_entities:
        enemy.update(tick,current_level,Chardude.Pos_x,Chardude.Pos_y, Chardude.Ghoststate, enemyAlertness)
        for bullet in enemy.CurrentBullets:
            current_bullets.append(bullet)
    for i in range(len(current_bullets)):
        current_bullets[i].update(tick,current_level,current_entities,Chardude)
    for bullet in current_bullets:
        if bullet.Pos_x < 0 or bullet.Pos_x > 1080 or bullet.Pos_y < 0 or bullet.Pos_y>720 or bullet.HasHit:
            current_bullets.remove(bullet)
    #print(current_bullets)
    if not Chardude.update(tick,current_level,current_entities):
        gameOver = True
    ## SOUND STUFF ##
    Sound.charsoundhandler.update(Chardude, tick)
    
    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    #screen.fill(WHITE)

    # --- Drawing code should go here
    if Chardude.Ghoststate:
        curr_color = RED
        txt_color = YELLOW
    else:
        curr_color = WHITE
        txt_color = BLACK

    for m in range(len(current_room)): #36
        for n in range(len(current_room[0])): #24
            text = Core.draw_tile.draw_tile(m, n, current_room, txt_color, screen, font25, Chardude.Ghoststate)

            #Blit in words here
            if text != None:
                screen.blit(text, [m*30,n*30])

    for entity in current_entities:
        entity.draw(tick,screen)
    Chardude.draw(tick,screen)


    for bullet in current_bullets:
        bullet.draw(tick,screen)

    #Stuff to insert in main() mainloop here (for textboxthatworks):
    
    #render text calls
    textbox.line1()
    textbox.line2()
    textbox.line3()
    textbox.line4()
    textbox.line5()
    #change textbox.shadow_percentage to change bar
    
    #switch text
    textbox.text[0] = "Shadow Bar," + str(textbox.shadow_percentage) + "% remaining"
    #textbox.shadow_bar(35)
    
    #Actual draws and loop mechs
    textbox.create_textbox()
    textbox.blitz()
    screen.blit(Chardude.currentpicture, (1150,590,124,120))

    Core.Cursor.DrawCursor(pygame, screen, Chardude.Ghoststate, Chardude.hasGun )

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    tick = clock.tick(60)

    if gameOver or gameWin: #manually reset gamemode
        if gameOver:
            GOscreen.GO(pygame, screen) #Game over screen
        else:
            WINscreen.WIN(pygame, screen)
        gameOver = False #start resetting all values
        gameWIN = False
        Chardude = Char.Character.Character();

        oldbody = [Char.Enemy.Enemy(50,50)];
        oldbody[0].images = [pygame.image.load('Art/Player_original_head.png'),pygame.image.load('Art/Arms.png')]
        oldbody[0].hasGun = False
        Chardude.absorb(oldbody,0);

        room_grid_position = [0,0]

        current_level = Core.Level.Level()
        current_level.load_level(1)
        current_room = current_level.get_current_room()
        current_bullets = []; # List of bullets in a room, reset on room change
        Chardude.Pos_x = current_level.start_position[0]
        Chardude.Pos_y = current_level.start_position[1]

        current_entities = current_level.get_current_entities()
        pygame.mouse.set_visible(True)
        if not TitleScreen.TitleScreen(pygame, screen): #launch title screen
            done = True
            pygame.quit()
            sys.exit()
        Sound.soundlib.play_music("Ambi.ogg", -1)



# Close the window and quit.
pygame.quit()
