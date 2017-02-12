import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (204, 0, 0)
YELLOW = (255, 215, 0)
GREY = (100,100,100)


def draw_tile(x, y, current_room, txt_color, screen, font25, isGhoststate):

    # Default Colour for non-defined tile id's
    curr_color = 'null'

    # Colours for tiles unaffected by ghost state
    if int( current_room[x][y] ) == -1:
        curr_color = BLACK
    if int( current_room[x][y] ) == 2:
        curr_color = [70,55,30]
    #if current_room[x][y] == 10:
        #curr_color = [140,100,80]

    if curr_color == "null":

        if int( current_room[x][y] ) in [0,3,5,6,7,8]:
            if isGhoststate:
                tile_image = pygame.image.load('Art/Floor_2_Red.png')
            else:
                tile_image = pygame.image.load('Art/Floor_2_White.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 1:
            if isGhoststate:
                tile_image = pygame.image.load('Art/Wall_2_Yellow.png')
            else:
                tile_image = pygame.image.load('Art/Wall_2_Blue.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 4:
            tile_image = pygame.image.load('Art/Portal_End.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 10:
            if int( current_room[x+1][y] ) == 10 and int( current_room[x][y+1] ) == 10 and int( current_room[x-1][y] ) != 10 and int( current_room[x][y-1] ) != 10:
                if isGhoststate:
                    below_tile_image = pygame.image.load('Art/Floor_2_Red.png')
                else:
                    below_tile_image = pygame.image.load('Art/Floor_2_White.png')
                for i in range(4):
                    bellow_imagerect = pygame.Rect(x*30+i*30, y*30, 30, 30)
                    screen.blit(below_tile_image, bellow_imagerect)
                    bellow_imagerect = pygame.Rect(x*30+i*30, y*30+30, 30, 30)
                    screen.blit(below_tile_image, bellow_imagerect)
                tile_image = pygame.image.load('Art/Table.png')
                imagerect = pygame.Rect(x*30, y*30, 30, 30)
                screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        # Image tiles
        if int( current_room[x][y] ) == 9:
            tile_image = pygame.image.load('Art/Control-panel-red.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 12:
            tile_image = pygame.image.load('Art/Locked.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 11:
            if isGhoststate:
                below_tile_image = pygame.image.load('Art/Floor_2_Red.png')
            else:
                below_tile_image = pygame.image.load('Art/Floor_2_White.png')
            bellow_imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(below_tile_image, bellow_imagerect)
            tile_image = pygame.image.load('Art/Bars-Vertical.png')
            if current_room[x+1][y] in [1,11] and current_room[x-1][y] in [1,11]:
                tile_image = pygame.image.load('Art/Bars-Horizontal.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 13:
            tile_image = pygame.image.load('Art/Control-panel-Green.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 14:
            tile_image = pygame.image.load('Art/Cracked-Wall.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 15:
            tile_image = pygame.image.load('Art/Package.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 16:
            tile_image = pygame.image.load('Art/Blue-Panel.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 17:
            tile_image = pygame.image.load('Art/Blue-Panel-Pressed.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 18:
            tile_image = pygame.image.load('Art/Red-Panel.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 19:
            tile_image = pygame.image.load('Art/Red-Panel-Pressed.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 20:
            tile_image = pygame.image.load('Art/Blue-Door.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 21:
            tile_image = pygame.image.load('Art/Red-Door.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 22:
            tile_image = pygame.image.load('Art/Green-Door.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

        elif int( current_room[x][y] ) == 23:
            tile_image = pygame.image.load('Art/Cyan-Door.png')
            imagerect = pygame.Rect(x*30, y*30, 30, 30)
            screen.blit(tile_image, imagerect)
            return font25.render('', True, txt_color)

    else:
        pygame.draw.rect(screen, curr_color, [x*30,y*30, 30, 30], 0) #col by row mat.
        if current_room[x][y] not in [-1,0,1,2,3,5,6,7,8,10,11]:
            text = font25.render(str(current_room[x][y]), True, txt_color)
            return text
        return font25.render('', True, txt_color)
