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


if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (200, 200, 0)
GREY = (100,100,100)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("No Swears Pls - Das Spiel")

font25 = pygame.font.SysFont('Calibri', 25, True, False)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Define
keys_pressed = []


objects = []

Chardude = Char.Character.Character();
group = pygame.sprite.Group(Chardude)

Command = Core.Command.Command();
tick = 0;


enemylist = []; # this is a temp thing
enemylist.append(Char.Enemy.Scientist(50,50));

oldbody = Char.Enemy.Enemy(50,50);
Chardude.Possessing = oldbody;

current_room = []
'''
In a room, currently the values for stuff are:
0 - empty air, no interaction
1 - wall, Char cannot move there
'''

room_grid_position = [0,0]

current_level = Core.Level.Level()
current_level.load_level(1)
current_room = current_level.get_current_room()

for m in range(len(current_room)):
    for n in range(len(current_room[m])):
        if current_room[m][n] == 3:
            Chardude.Pos_x = 30 * m
            Chardude.Pos_y = 30 * n
        elif current_room[m][n] == 5:
            current_level.get_current_entities().append(Char.Enemy.Guard(m*30,n*30));

current_entities = current_level.get_current_entities()

#make 36 x 24 matrix
#temporary, will eventually pickle
#for now, walls around outside
'''
for m in range (36):
    current_room.append([])
    for n in range (24):
        if m==0 or m==35 or n==0 or n==23:
            current_room[m].append(1)
        else:
            current_room[m].append(0)
'''

#30x30 px, 36 x 24 grid
#Function for square draw
def draw_tile(x, y, state_counter, curr_color, txt_color):

    if current_room[x][y] == -1:
        curr_color = BLACK
    if current_room[x][y] == 2:
        curr_color = [70,55,30]
    if current_room[x][y] == 10:
        curr_color = [140,100,80]

    if Chardude.Ghoststate:
        if current_room[x][y] == 1:
            curr_color = YELLOW
        if current_room[x][y] == 11:
            curr_color = [150,150,0]
    else:
        if current_room[x][y] == 1:
            curr_color = GREY
        if current_room[x][y] == 11:
            curr_color = [150,150,150]

    pygame.draw.rect(screen, curr_color, [x*30,y*30, 30, 30], 0) #col by row mat.
    if current_room[x][y] not in [-1,0,1,2,3,5,10,11]:
        text = font25.render(str(state_counter), True, txt_color)
        return text
    return font25.render(str(""), True, txt_color)


def empty():
    print('Empty Floor Tile')
def wall():
    print('Wall Tile')
def door():
    print('Door Tile')
tiles = {0: empty, 1: wall, 2: exit}


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        #if event key down
        elif event.type == pygame.KEYDOWN:
            keys_pressed.append(event.key);
        elif event.type == pygame.KEYUP:
            keys_pressed.remove(event.key);
        Command.makeFromEvent(event);
        Chardude.getCommand(Command);

    # --- Game logic should go here
    current_tile = Chardude.getTile()
    print(current_tile)
    if current_tile[0] % 35 == 0 or current_tile[1] % 23 == 0:
        current_level.enter_door(current_tile, Chardude)
        current_room = current_level.get_current_room()
        current_entities = current_level.get_current_entities()
    for enemy in current_entities:
        enemy.update(tick)
    Chardude.update(tick,current_room,current_entities)


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
            xVal = m
            yVal = n
            text = draw_tile(xVal, yVal, current_room[m][n], curr_color, txt_color)

            #Blit in words here
            screen.blit(text, [xVal*30,yVal*30])

    group2 = pygame.sprite.Group(current_entities)


    group.draw(screen);
    group2.draw(screen);

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    tick = clock.tick(60)

# Close the window and quit.
pygame.quit()
