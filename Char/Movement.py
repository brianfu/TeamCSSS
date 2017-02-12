import pygame

def tryMoveTo(curr_x, curr_y, fut_x, fut_y, width, height, current_level, isAGhost):
    gridpos_x = int(fut_x//30)
    gridpos_y = int(fut_y//30)
    
    current_room = current_level.get_current_room()
    
    ## TRY MOVING X FIRST ##
    canmovex = True
    if fut_x > 1075 - width or fut_x < 0:
        canmovex = False
    elif curr_x == fut_x:
        canmovex = False
    else:
        xrect = pygame.Rect( fut_x, curr_y, width, height)
        for x in range(width//30 + 2):
            for y in range(height//30 + 2):
                if xrect.colliderect(
                pygame.Rect( (gridpos_x+x)*30,  (gridpos_y+y)*30,  30,  30)#rect of a tile
                ):
                    if current_room[gridpos_x+x][gridpos_y+y] == 1:
                        canmovex = False
                        break
                    elif current_room[gridpos_x+x][gridpos_y+y] in (10, 11, 12) and isAGhost==False:
                        canmovex = False
                        break
    if canmovex:
            curr_x = fut_x
            
    ## NOW TRY Y ##
    canmovey = True
    if fut_y > 715 - height or fut_y < 0:
        canmovey = False
    elif curr_y == fut_y:
        canmovey = False
    else:
        yrect = pygame.Rect( curr_x, fut_y, width, height)
        for x in range(width//30 + 2):
            for y in range(height//30 + 2):
                if yrect.colliderect(
                pygame.Rect( (gridpos_x+x)*30,  (gridpos_y+y)*30,  30,  30)#rect of a tile
                ):
                    if current_room[gridpos_x+x][gridpos_y+y] == 1:
                        canmovey = False
                        break
                    elif current_room[gridpos_x+x][gridpos_y+y] in (10, 11, 12) and isAGhost==False:
                        canmovey = False
                        break
    if canmovey:
        curr_y = fut_y
    
    return curr_x,curr_y
    
