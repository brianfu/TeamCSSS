import pygame

def tryMoveTo(curr_x, curr_y, fut_x, fut_y, width, height, current_level, isAGhost, chartype):
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
                    if int(current_room[gridpos_x+x][gridpos_y+y]) == 1:
                        canmovex = False
                        break
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) in (10, 11, 12, 14, 15) and isAGhost==False:
                        canmovex = False
                        break
                    
                    # Special Doors
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) == 20 and chartype != "Guard":
                        canmovex = False
                        break
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) == 21 and chartype != "Soldier":
                        canmovex = False
                        break
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) == 22 and chartype != "Janitor":
                        canmovex = False
                        break
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) == 23 and chartype != "Scientist":
                        canmovex = False
                        break
                    
                    # Button stuff
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) ==  16 and isAGhost == True:
                        current_level.activate_room_ether_button()
                        current_level.check_room_buttons()
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) ==  18 and isAGhost == False:
                        current_level.activate_room_regular_button()
                        current_level.check_room_buttons()
                        
                    if int(current_room[gridpos_x+x][gridpos_y+y]) not in (16, 17) and current_level.get_room_ether_b_state() == 1:
                        current_level.deactivate_room_ether_button()
                    if int(current_room[gridpos_x+x][gridpos_y+y]) not in (18, 19) and current_level.get_room_reg_b_state() == 1:
                        button_held = False
                        for enemy in current_level.get_current_entities():
                            e_gridpos_x = int((enemy.Pos_x)//30)
                            e_gridpos_y = int((enemy.Pos_y)//30)
                            if int(current_room[e_gridpos_x][e_gridpos_y]) in (18, 19):
                                button_held = True
                        if not button_held:
                            current_level.deactivate_room_regular_button()                  
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
                    if int(current_room[gridpos_x+x][gridpos_y+y]) == 1:
                        canmovey = False
                        break
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) in (10, 11, 12, 14, 15) and isAGhost==False:
                        canmovey = False
                        break
                    
                    # Special Doors
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) == 20 and chartype != "Guard":
                        canmovey = False
                        break
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) == 21 and chartype != "Soldier":
                        canmovey = False
                        break
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) == 22 and chartype != "Janitor":
                        canmovey = False
                        break
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) == 23 and chartype != "Scientist":
                        canmovey = False
                        break                    
                    
                    # Button stuff
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) ==  16 and isAGhost == True:
                        current_level.activate_room_ether_button()
                        current_level.check_room_buttons()
                    elif int(current_room[gridpos_x+x][gridpos_y+y]) ==  18 and isAGhost == False:
                        current_level.activate_room_regular_button()
                        current_level.check_room_buttons()
                        
                    if int(current_room[gridpos_x+x][gridpos_y+y]) not in (16, 17) and current_level.get_room_ether_b_state() == 1:
                        current_level.deactivate_room_ether_button()
                    if int(current_room[gridpos_x+x][gridpos_y+y]) not in (18, 19) and current_level.get_room_reg_b_state() == 1:
                        button_held = False
                        for enemy in current_level.get_current_entities():
                            e_gridpos_x = int((enemy.Pos_x)//30)
                            e_gridpos_y = int((enemy.Pos_y)//30)
                            if int(current_room[e_gridpos_x][e_gridpos_y]) in (18, 19):
                                button_held = True
                        if not button_held:
                            current_level.deactivate_room_regular_button()                     
    if canmovey:
        curr_y = fut_y
    
    return curr_x,curr_y
    
