import pygame
import os
import math

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except:
        print('Cannot load image:',name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Character(pygame.sprite.Sprite):


    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Ghoststate = False
        self.AttemptUnghost = False
        self.AttemptGhost = False
        
        self.Possessing = 0
        
        self.Pos_x = 50;
        self.Pos_y = 50;
        self.Timecountdown = 200 #at 60fps, the number should be 60*time wanted
        #self.Direction = 0; #can be 0-7,
        self.Orientation = 0; #can be 0-3
        self.Velocity = 216 #pixels / second
        self.Direction = [0,0,0,0]
        self.images = [pygame.image.load('Art/Char_0.jpg'),pygame.image.load('Art/Char_1.png')]
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,30,30)


    def unGhost(self,current_room,enemylist):
        self.AttemptUnghost = False
        for i in range(len(enemylist)):
            if enemylist[i].Possessable and self.rect.colliderect(enemylist[i].rect):
                self.Possessing = enemylist.pop(i)
                self.Ghoststate = False
                self.Pos_x = self.Possessing.Pos_x
                self.Pos_y = self.Possessing.Pos_y
                self.images[0] = self.Possessing.images[0]
                return
        return
    
    
    def goGhost(self,current_room,enemylist):
        self.AttemptGhost = False
        if self.Possessing == 0:
            return
        self.Possessing.Pos_x = 30*(math.floor(self.Pos_x/30 + .5))
        self.Possessing.Pos_y = 30*(math.floor(self.Pos_y/30 + .5))
        enemylist.append(self.Possessing)
        self.Possessing = 0
        self.Ghoststate = True
        return


    def update(self,tick,current_room,enemylist):
        
        self.move(tick,current_room)

        if self.AttemptGhost:
            self.goGhost(current_room,enemylist);
            
        if self.AttemptUnghost:
            self.unGhost(current_room, enemylist);

        if self.Ghoststate:
            self.image = self.images[1];
        else: self.image = self.images[0];
        

    def move(self,tick,current_room):
        deltamove = [0,0];
        for i in range(4):
            if i==3 or i==2:
                deltamove[i%2] += self.Direction[i]* -1;
            else:
                deltamove[i%2] += self.Direction[i]; #add 1 to deltamove if 0 or 1, minus 1 if 2 or 3
        future_Pos_x = self.Pos_x
        future_Pos_y = self.Pos_y
        if deltamove[0] != 0 and deltamove[1] != 0:
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000) * 0.7
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000) * 0.7
        else:
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000)
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000)

        if current_room[int(math.floor(future_Pos_x/30))][int(math.floor(self.Pos_y/30))] != 1 and current_room[int(math.floor((future_Pos_x+30)/30))][int(math.floor((self.Pos_y+30)/30))] != 1:
            self.Pos_x = future_Pos_x
            
        if current_room[int(math.floor(self.Pos_x/30))][int(math.floor(future_Pos_y/30))] != 1 and current_room[int(math.floor((self.Pos_x+30)/30))][int(math.floor((future_Pos_y+30)/30))] != 1:
            self.Pos_y = future_Pos_y
            
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,30,30)


    def getCommand(self,command):
        if command.ctype == "go_dir":
            self.Orientation = command.spec;
            self.Direction[command.spec] = 1;
            
        elif command.ctype == "stop_dir":
            self.Direction[command.spec] = 0;
        
        elif command.ctype == "ghost_mode":
            if command.spec == "swap":
                if self.Ghoststate:
                    self.AttemptUnghost = True;
                else:
                    self.AttemptGhost = True;


    def getTile(self):
        return [int(math.floor(self.Pos_x/30 + 0.5)),int(math.floor(self.Pos_y/30 + 0.5))]
        
   


'''
    def draw(self,screen):
        self.image.draw(screen);
        return 0; #Update later with drawing stuff'''
