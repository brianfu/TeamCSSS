"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
from pygame.locals import *
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1280, 720)

screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Grid")
 
font = pygame.font.SysFont('Calibri', 25, True, False)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Define
space_pressed = False
position = [0,0] #0-35, 0-23, col by row, increment row until 23, then reset and increment col
current_pos = [0,0]
state_counter = 0 #0-3, increment if spacebar
s_c_list = []
n_list = []

#this doesnt work
#make 36 x 24 matrix
for n in range (24):
    n_list.append(0)
for m in range (36):
    s_c_list.append(n_list)

'''
for m in range (36):
    s_c_list.append([])
    for n in range (24):
        s_c_list[m].append(0)
'''

#30x30 px, 36 x 24 grid
#Function for square draw
def draw_square(position, state_counter, color):
    #do in mainloop: if position is same as current position, change colors
    pygame.draw.rect(screen, color, [position[0]*30,position[1]*30, 30, 30], 0) #col by row mat.
    text = font.render(str(state_counter), True, BLACK)
    return text
    #bilt in mainloop "screen.blit(text, [position[0]*30, position[1]*30])"
    
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        #if event key down
        elif event.type == pygame.KEYDOWN:
            #print(current_pos);
            
            #if pressed space
            if event.key == pygame.K_SPACE:
                if state_counter >= 3:
                    state_counter = 0
                else:
                    state_counter += 1
                    
                #might as well do flag
                space_pressed = True
                    
            #Move keys
            elif event.key == pygame.K_RIGHT:
                #print("SHIT IS FUCKED")
                if current_pos[0] >= 35:
                    current_pos[0] = 0
                else:
                    current_pos[0] += 1
            elif event.key == pygame.K_LEFT:
                if current_pos[0] <= 0:
                    current_pos[0] = 35
                else:
                    current_pos[0] -= 1
            elif event.key == pygame.K_DOWN:
                if current_pos[1] >= 23:
                    current_pos[1] = 0
                else:
                    current_pos[1] += 1
            elif event.key == pygame.K_UP:
                if current_pos[1] <= 0:
                    current_pos[1] = 23
                else:
                    current_pos[1] -= 1
            #ik i fucked up the order dw bout it
                   
    #text = draw_square([2,2], state_counter, GREEN)
    #screen.blit(text, [2*30,2*30])
    
    
    # --- Game logic should go here
    for m in range (len(s_c_list)): #36
        for n in range (len(n_list)): #24
            #Find and draw current position
            position = [m,n]
            if position == current_pos:
                text = draw_square(position, state_counter, GREEN)
                #add to and check for overflow in state counter ([0,3] only)
                #if space_pressed:
                #   s_c_list[m][n] = s_c_list[n][m] + 1               
            else:
                text = draw_square(position, state_counter, RED)
        
            #Bilt in words here
            screen.blit(text, [position[0]*30,position[1]*30])
            
            
            #position[1] += 1 #iterator #these don't work
        #position[0] += 1
    
    #Reset space_pressed flag
    space_pressed = False
    
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    #screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()