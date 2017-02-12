import pygame
import os
import math
import time
import Char.Movement

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

class Character(object):

    def __init__(self):
        self.Ghoststate = False
        self.AttemptUnghost = False
        self.AttemptGhost = False

        self.Possessing = 0

        self.PlayGhostSound = False
        self.Hitpoints = 50
        self.Dead = False
        self.Pos_x = 50;
        self.Pos_y = 50;
        self.size = [38,38];
        
        self.Timecountdown = 200 #at 60fps, the number should be 60*time wanted
        self.Orientation = 0; #can be 0-7
        self.Velocity = 110 #pixels / second
        self.MaxVelocity = 220
        self.Direction = [0,0,0,0]
        
        self.ghostimages = [pygame.image.load('Art/Player_alt_dimension_head.png'),pygame.image.load('Art/Player_arms_alt_dimension.png')]
        self.absorbedimages = []
        self.portalimage = pygame.image.load('Art/Portal.png')
        
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size[0],self.size[1])
        self.timer = 0;
        self.Moving = False;
        self.hasGun = False;
        self.currentpicture = pygame.image.load('Art/Player_Portrait.png')
        self.ghostTimer = 10000
        self.portalvalue = 0

    def absorb(self,enemylist,index):
        self.Possessing = enemylist.pop(index)
        self.Ghoststate = False
        self.Pos_x = self.Possessing.Pos_x
        self.Pos_y = self.Possessing.Pos_y
        self.Orientation = self.Possessing.Orientation
        self.absorbedimages = self.Possessing.images
        self.hasGun = self.Possessing.hasGun
        self.currentpicture = self.Possessing.currentpicture

    def unGhost(self,current_room,enemylist):
        self.AttemptUnghost = False
        for i in range(len(enemylist)):
            if enemylist[i].Possessable and self.rect.colliderect(enemylist[i].rect):
                self.absorb(enemylist,i);
                self.portalvalue = 15
                self.PlayGhostSound = True
                return
        return

    def goGhost(self,current_room,enemylist):
        self.AttemptGhost = False
        if self.Possessing == 0:
            return
        self.Possessing.Pos_x = self.Pos_x
        self.Possessing.Pos_y = self.Pos_y
        self.Possessing.Incapacitated = True
        self.Possessing.IncapacitatedTimer = 120
        enemylist.append(self.Possessing)
        
        self.Possessing = 0
        self.Ghoststate = True
        self.PlayGhostSound = True
        self.hasGun = False
        self.countdowntime = time.time()
        self.currentpicture = pygame.image.load("Art/Player-Ghost-Portrait.png")
        self.portalvalue = -15
        return

    def update(self,tick,current_level,enemylist):

        if self.checkWin(current_level):
            return 1        

        current_room = current_level.get_current_room();

        self.move(tick,current_level)

        if self.AttemptGhost:
            self.goGhost(current_room,enemylist);

        if self.AttemptUnghost:
            self.unGhost(current_room, enemylist);

        if self.Ghoststate:
            self.ghostTimer -= tick
            if self.ghostTimer < 0:
                return -1
        else:
            self.ghostTimer += 2*tick
            self.ghostTimer = min(self.ghostTimer, 10000)
        return 0

    def setOrientation(self,deltamove):
        if deltamove[0]==1:
            if deltamove[1]==0:
                self.Orientation = 0;
            elif deltamove[1]==-1:
                self.Orientation = 7;
            elif deltamove[1]==1:
                self.Orientation = 1;
        elif deltamove[0]==0:
            if deltamove[1]==-1:
                self.Orientation = 6;
            elif deltamove[1]==1:
                self.Orientation = 2;
        else:
            if deltamove[1]==0:
                self.Orientation = 4;
            elif deltamove[1]==-1:
                self.Orientation = 5;
            else:
                self.Orientation = 3;

    def move(self,tick,current_level):
        current_room = current_level.get_current_room()
        deltamove = [0,0];
        for i in range(4):
            if i==3 or i==2:
                deltamove[i%2] += self.Direction[i]* -1;
            else:
                deltamove[i%2] += self.Direction[i]; #add 1 to deltamove if 0 or 1, minus 1 if 2 or 3
        future_Pos_x = self.Pos_x
        future_Pos_y = self.Pos_y

        if deltamove[0]!=0 or deltamove[1]!=0:
            self.Velocity += (3*tick)//5
            self.Velocity = min(self.Velocity,self.MaxVelocity)
            self.setOrientation(deltamove)
            self.Moving = True
        else:
            self.Velocity -= (3*tick)//5
            self.Velocity = max(self.Velocity,self.MaxVelocity/2)
            self.Moving = False

        if deltamove[0] != 0 and deltamove[1] != 0:
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000) * 0.7
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000) * 0.7
        else:
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000)
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000)

        if not self.Ghoststate:
            PlayerType = self.Possessing.Name
        else:
            PlayerType = "Player"

        self.Pos_x,self.Pos_y = Char.Movement.tryMoveTo(self.Pos_x,self.Pos_y,
            future_Pos_x,future_Pos_y,
            self.size[0],self.size[1],
            current_level,self.Ghoststate,PlayerType)

        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size[0],self.size[1])

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
        return [int(math.floor((self.Pos_x+self.size[0]/2)/30)),int(math.floor((self.Pos_y + self.size[1]/2)/30))]

    def draw(self,tick,screen):
        ##PORTALROTATEOUT##
        if self.portalvalue < 0:
            self.portalvalue += 1;
            port = pygame.transform.rotozoom(self.portalimage, (self.portalvalue)*-30, (14+self.portalvalue)/14)
            prect = port.get_rect();
            screen.blit(port,[self.Pos_x + 19 - prect.center[0], self.Pos_y + 19 - prect.center[1]])
            return
        if self.Ghoststate:
            drawimages = self.ghostimages
        else:
            drawimages = self.absorbedimages
        self.timer += tick;
        self.timer %= 1000
        angle = 0
        angle += 45*self.Orientation
        head = pygame.transform.rotate(drawimages[0],angle)
        if self.Moving:
            angle += 15*math.sin(2*math.pi*self.timer/1000)
        arms = pygame.transform.rotate(drawimages[1],angle)
        arect = arms.get_rect();
        hrect = head.get_rect();
        armcenter = list(arect.center)
        headcenter =list(hrect.center)
        angle = math.pi*self.Orientation/4
        if self.hasGun:
            armcenter[0]-=9*math.sin(angle)
            armcenter[1]-=9*math.cos(angle)
        screen.blit(arms,[self.Pos_x + 19 - armcenter[0],self.Pos_y + 19 - armcenter[1]])
        screen.blit(head,[self.Pos_x + 19 - headcenter[0],self.Pos_y + 19 - headcenter[1]])
        ##PORTALROTATEIN##
        if self.portalvalue > 0:
            self.portalvalue -= 1;
            port = pygame.transform.rotozoom(self.portalimage, (14-self.portalvalue)*30, self.portalvalue/14)
            prect = port.get_rect();
            screen.blit(port,[self.Pos_x + 19 - prect.center[0], self.Pos_y + 19 - prect.center[1]])
        
        
    def shoot(self):
        print("Hi")

    def checkWin(self, current_level):
        gridpos_x = int(self.Pos_x//30)
        gridpos_y = int(self.Pos_y//30)
        
        current_room = current_level.get_current_room()
        
        if current_room[gridpos_x][gridpos_y] == 4:
            return True
        else:
            return False



'''
    def draw(self,screen):
        self.image.draw(screen);
        return 0; #Update later with drawing stuff'''
