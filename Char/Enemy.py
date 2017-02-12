import pygame
import os
from random import randrange
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

class Enemy(pygame.sprite.Sprite):

    def __init__(self,newX,newY):
        pygame.sprite.Sprite.__init__(self)
        self.Possessedstate = False
        self.Pos_x = newX;
        self.Pos_y = newY;
        self.EnemyType = 0
        self.Possessable = True
        self.EnemyType = 0 
        self.Hitpoints = 1
        self.Armour = 0
        self.AttackDamage = 0
        self.SpecialTraits = 0 #Special Traits are stored as integers and checked for as integers.
        self.Alerted = 0
        self.Direction = 0; #can be 0-7,
        self.Orientation = 0 #can be 0-3
        self.Velocity = 216 #pixels / second
        self.Direction = [0,0,0,0]
        self.images = [pygame.image.load('Art/Char_0.jpg'),pygame.image.load('Art/Char_1.png')]
        self.image = self.images[0]
        self.size = [40,40]
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size[0],self.size[1])
        self.PatrolCycleLength = 0
        self.Moving = False
        self.StopTime = 0

    def update(self,tick,current_room,char_x,char_y):
        if (self.Alerted==0):
            self.PatrolCycle()
        elif(self.Alerted==1):
            self.Chase(char_x, char_y)
        #elif(self.Alerted==2):
            #self.Flee(char_x, char_y)

        self.move(tick,current_room)

        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,30,30)
    
    def PatrolCycle(self):
        self.PatrolCycleLength += 1
        if(self.PatrolCycleLength>=30):
            self.PatrolCycleLength = 0;
            if(self.Moving==True):
                x = randrange(0,2)
                if (x==0):
                    self.Moving=False
                    self.Direction = [0,0,0,0]
                    self.StopTime = 2
            else:
                self.StopTime -= 1
                if (self.StopTime<=0):
                    self.Moving=True
                    w=0
                    while(w<1):
                        i = randrange(0,3) #Up or Down or Neither?
                        if(i==0):
                            self.Direction[0]=1
                            w+=1
                        elif(i==1):
                            self.Direction[2]=1
                            w+=1
                        j = randrange(0,3) #Right or Left or Neither?
                        if(j==0):
                            self.Direction[1]=1
                            w+=1
                        elif(j==1):
                            self.Direction[3]=1
                            w+=1
    
    def Chase(self, target_x, target_y): #target_x should be Character.Pos_x, target_y should be Character.Pos_y
        A=self.Pos_y-target_y #gives directional vectors with Enemy at point of origin
        B=self.Pos_x-target_x
        A_neg = False
        if(A<0):    #Only dealing with directional vector above X-axis (cartesian quardinate plane with Enemy at origin)
            A_neg = True
            A = -A
        if(B!=0):
            R = A/B #Avoiding ripping a hole in the universe
            if (0<=R or R<2.4142):
                self.Direction[1]=1 #Right
            if(-2.4142<R or R<=0):
                self.Direction[3]=1 #Left
            if(R<= -0.4142 or 0.4142<=R):
                if(A_neg):
                    self.Direction[0]=1 #Down
                else:
                    self.Direction[2]=1 #Up
        elif(B==0): #Pretty much case where B approaches infinity and negative infinity
            if(A_neg):
                self.Direction[0]=1 #Down
            else:
                self.Direction[2]=1 #Up

    #def Flee():
                          
    def move(self,tick,current_room):
        #Turn Cartesian Direction Vector[4] to Python directional Vector[2]
        deltamove = [0,0];
        for i in range(4):
            if i==3 or i==2:
                deltamove[i%2] += self.Direction[i]* -1;
            else:
                deltamove[i%2] += self.Direction[i]; #add 1 to deltamove if 0 or 1, minus 1 if 2 or 3
        #Find Pos_x and Pos_y
        future_Pos_x = self.Pos_x
        future_Pos_y = self.Pos_y
        #Compensate for diagonal movement
        if deltamove[0] != 0 and deltamove[1] != 0:
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000) * 0.7
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000) * 0.7
        else:
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000)
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000)
        
        gridpos_x = int(future_Pos_x//30)
        gridpos_y = int(future_Pos_y//30)
        canmovex = True
        if future_Pos_x > 1075 - self.size[0] or future_Pos_x < 0:
            canmovex = False
        else:
            xrect = pygame.Rect(  future_Pos_x,  self.Pos_y,  self.size[0],  self.size[1])
            for x in (0,1,2):
                for y in (0,1,2):
                    if xrect.colliderect(
                    pygame.Rect( (gridpos_x+x)*30,  (gridpos_y+y)*30,  30,  30) ):
                        if current_room[gridpos_x+x][gridpos_y+y] in (1, 2, 4, 9, 10, 11, 12):
                            canmovex = False
                            break
                        
        if canmovex:
            self.Pos_x = future_Pos_x
        canmovey = True
        if future_Pos_y > 715 - self.size[1] or future_Pos_y < 0:
            canmovey = False
        else:
            yrect = pygame.Rect(  self.Pos_x,  future_Pos_y,  self.size[0],  self.size[1])
            for x in (0,1,2):
                for y in (0,1,2):
                    if yrect.colliderect(
                    pygame.Rect( (gridpos_x+x)*30,  (gridpos_y+y)*30,  30,  30) ):
                        if current_room[gridpos_x+x][gridpos_y+y] in (1, 2, 4, 9, 10, 11, 12):
                            canmovey = False
                            break

        if canmovey:
            self.Pos_y = future_Pos_y

        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size[0],self.size[1])        
    
    def getCommand(self,command):
        if command.ctype == "keypress":
            if command.spec == "DOWN":
                self.Orientation = 0;
                self.Direction[0] = 1;
            elif command.spec == "RIGHT":
                self.Orientation = 1;
                self.Direction[1] = 1;
            elif command.spec == "UP":
                self.Orientation = 2;
                self.Direction[2] = 1;
            elif command.spec == "LEFT":
                self.Orientation = 3;
                self.Direction[3] = 1;
        elif command.ctype == "keydepress":
            if command.spec == "DOWN":
                self.Direction[0] = 0;
            elif command.spec == "RIGHT":
                self.Direction[1] = 0;
            elif command.spec == "UP":
                self.Direction[2] = 0;
            elif command.spec == "LEFT":
                self.Direction[3] = 0;
    def getTile(self):
        return [int(math.floor(self.Pos_x/30)),int(math.floor(self.Pos_y/30))]
'''
    def draw(self,screen):
        self.image.draw(screen);
        return 0; #Update later with drawing stuff'''
class Guard(Enemy):
    def __init__(self,newX,newY):
        Enemy.__init__(self,newX,newY)
        Enemy.EnemyType = 1
        Enemy.Hitpoints = 100
        Enemy.Armour = 1
        Enemy.AttackDamage = 2
        Enemy.SpecialTraits = 0
        #Enemy.images = #NEED TO ADD ENEMY IMAGES#

class Scientist(Enemy):
    def __init__(self,newX,newY):
        Enemy.__init__(self,newX,newY)
        self.EnemyType = 2
        Enemy.Hitpoints = 50
        Enemy.Armour = 0
        Enemy.AttackDamage = 0
        Enemy.SpecialTraits = 0
        #Enemy.images = #NEED TO ADD ENEMY IMAGES#
