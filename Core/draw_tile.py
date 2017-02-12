import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (204, 0, 0)
YELLOW = (255, 215, 0)
GREY = (100,100,100)


def draw_tile(x, y, current_room, txt_color, screen, font25, isGhoststate):
    curr_color = WHITE
    if current_room[x][y] == -1:
        curr_color = BLACK
    if current_room[x][y] == 2:
        curr_color = [70,55,30]
    if current_room[x][y] == 10:
        curr_color = [140,100,80]

    if isGhoststate:
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
        text = font25.render(str(current_room[x][y]), True, txt_color)
        return text
    return font25.render('', True, txt_color)
