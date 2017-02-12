import pygame
import os
import random

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
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,30,30)
        self.PatrolCycleLength = 0
        self.Moving = False
        self.StopTime = 0

    def update(self,tick, current_room):
        if (Alerted==0):
            self.PatrolCycle()
        #else

        self.move(tick,current_room)

        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,30,30)
    
    def PatrolCycle():
        PatrolCycleLength += 1
        if(PatrolCycleLength==30)
            if(Moving==True)
                x = randrange(0,1,1)
                if (x==0)
                    Moving=False
                    Direction = [0,0,0,0]
                    StopTime = 120
            else
                StopTime -= 1
                if (StopTime<=0):
                    Moving=True
                    w=0
                    while(w<1)
                        i = randrange(0,2,1) #Up or Down or Neither?
                        if(i==0)
                            Direction[0]=1;
                            w+=1
                        elif(i==1)
                            Direction[2]=1;
                            w+=1
                        j = randrange(0,2,1) #Right or Left or Neither?
                        if(j==0)
                            Direction[1]=1;
                            w+=1
                        elif(j==1)
                            Direction[3]=1;
                            w+=1
    
    #def Chase():

                              
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
        #Move if there is no wall
        if current_room[int(math.floor(future_Pos_x/30))][int(math.floor(self.Pos_y/30))] != 1 and current_room[int(math.floor((future_Pos_x+30)/30))][int(math.floor((self.Pos_y+30)/30))] != 1:
            self.Pos_x = future_Pos_x

        if current_room[int(math.floor(self.Pos_x/30))][int(math.floor(future_Pos_y/30))] != 1 and current_room[int(math.floor((self.Pos_x+30)/30))][int(math.floor((future_Pos_y+30)/30))] != 1:
            self.Pos_y = future_Pos_y

        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,30,30)
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
