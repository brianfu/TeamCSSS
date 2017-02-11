import os, sys
import pygame
from pygame.locals import *
import Core.load_sound
import Core.load_image
import Core.Command
import Char.Character


if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (1280, 720)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Ghost in the fuck you")

font25 = pygame.font.SysFont('Calibri', 25, True, False)

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Define
keys_pressed = []

objects = []

Char = Char.Character.Character();
group = pygame.sprite.Group(Char)

Command = Core.Command.Command();
tick = 0;

current_room = [] 
'''
In a room, currently the values for stuff are:
0 - empty air, no interaction
1 - wall, Char cannot move there
'''

room_grid_position = [0,0]

#make 36 x 24 matrix
#temporary, will eventually pickle
#for now, walls around outside
for m in range (36):
    current_room.append([])
    for n in range (24):
        if m==0 or m==35 or n==0 or n==23:
            current_room[m].append(1)
        else:
            current_room[m].append(0)

#30x30 px, 36 x 24 grid
#Function for square draw
def draw_square(x, y, state_counter, color):
    pygame.draw.rect(screen, color, [x*30,y*30, 30, 30], 0) #col by row mat.
    text = font25.render(str(state_counter), True, BLACK)
    return text


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
        Char.getCommand(Command);

    # --- Game logic should go here
    Char.update(tick)
    #Reset space_pressed flag
    space_pressed = False

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    #screen.fill(WHITE)

    # --- Drawing code should go here
    for m in range(len(current_room)): #36
        for n in range(len(current_room[0])): #24
            xVal = m
            yVal = n
            text = draw_square(xVal, yVal, current_room[m][n], WHITE)

            #Blit in words here
            screen.blit(text, [xVal*30,yVal*30])
           
    group.draw(screen);
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    tick = clock.tick(60)

# Close the window and quit.
pygame.quit()


