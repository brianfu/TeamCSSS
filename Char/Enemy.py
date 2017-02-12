import pygame
import os
from random import randrange
import math
import Core.Bullet
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

class Enemy(object):

    def __init__(self,newX,newY):
        pygame.sprite.Sprite.__init__(self)
        self.Possessedstate = False
        self.Pos_x = newX;
        self.Pos_y = newY;
        self.EnemyType = 0
        self.Possessable = True
        self.hasGun = True
        self.Hitpoints = 1
        self.Armour = 0
        self.AttackDamage = 0
        self.SpecialTraits = 0 #Special Traits are stored as integers and checked for as integers.
        self.Alerted = 1
        self.Orientation = 0 #can be 0-7
        self.Velocity = 216 #pixels / second
        self.Direction = [0,0,0,0]
        self.images = [pygame.image.load('Art/Blue_hat_guard.png'),pygame.image.load('Art/Arms.png')]
        #self.image = self.images[0]
        self.size = [38,38]
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size[0],self.size[1])
        self.PatrolCycleLength = 0
        self.Moving = False
        self.StopTime = 0
        self.FireCooldown = 0
        self.Name = "Giorgio"
        self.timer = 0;
        self.CurrentBullets = []
        self.Incapacitated = False
        self.IncapacitatedTimer = 0
        self.Alertness = 0
        self.currentpicture = pygame.image.load('Art/Player_Portrait.png')
        #self.Alerted = 0

    def update(self,tick,current_level,char_x,char_y, ghosted, newAlertnessLevel):
        current_room = current_level.get_current_room()
        self.Alertness = newAlertnessLevel
        
        if (self.Incapacitated):
            if (self.IncapacitatedTimer > 0):
                self.IncapacitatedTimer -= 1
                return
            else:
                self.Incapacitated = False
        
        if (self.Alertness < 1):
            self.PatrolCycle(current_room)
        elif(self.Alertness>1):
            self.Direction = [0,0,0,0]
            self.Chase(char_x, char_y)
        elif(self.Alertness>20):
            self.Direction = [0,0,0,0]
            self.Flee(char_x, char_y)

        self.move(tick,current_level)

        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size[0],self.size[1])
    
    def PatrolCycle(self, current_room):
        #gridPos = self.getTile()
        #currentPath = str( current_room[gridPos[0]][gridPos[1]] ) - int( current_room[gridPos[0]][gridPos[1]] )[-1]
        #print( currentPath )
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
        gridpos_x=int((self.Pos_x+20)//30)
        gridpos_y=int((self.Pos_y+20)//30)
        if(self.Moving==True):
            if(self.Direction[0]==1):
                if(current_room[gridpos_x][gridpos_y+1]!=0):
                    self.Direction[0]=0
                    self.Direction[2]=1
            if(self.Direction[1]==1):
                if(current_room[gridpos_x+1][gridpos_y]!=0):
                    self.Direction[1]=0
                    self.Direction[3]=1
            if(self.Direction[2]==1):
                if(current_room[gridpos_x][gridpos_y-1]!=0):
                    self.Direction[2]=0
                    self.Direction[0]=1
            if(self.Direction[3]==1):
                if(current_room[gridpos_x-1][gridpos_y]!=0):
                    self.Direction[3]=0
                    self.Direction[1]=1
    
    def Chase(self, target_x, target_y): #target_x should be Character.Pos_x, target_y should be Character.Pos_y
        A=self.Pos_y-target_y #gives directional vectors with Enemy at point of origin
        B=target_x-self.Pos_x
        C=A*A + B*B
        clip_size = 2
        if(C>=20000 and self.StopTime==0): #More than 200 pixels away, C>200^2
            self.Moving = True
            A_neg = False
            if(A<0):    #Only dealing with directional vector above X-axis (cartesian quardinate plane with Enemy at origin)
                A_neg = True
                A = -A
            if(B!=0):
                R = A/B #Avoiding ripping a hole in the universe
                if (0<=R and R<2.4142):
                    self.Direction[1]=1 #Right
                if(-2.4142<R and R<=0):
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
        elif(C<20000):
            self.Moving = False
            self.Direction = [0,0,0,0]
            if(self.StopTime==0):
                self.StopTime = 60
        if(self.StopTime>0):
            if(self.StopTime%(60/clip_size)==0):
                self.CurrentBullets.append(Core.Bullet.Bullet(self.Pos_x, self.Pos_y, target_x, target_y, False))
        if(self.Moving==False and self.StopTime>0):
            self.StopTime -= 1

    def Flee(self, target_x, target_y): #target_x should be Character.Pos_x, target_y should be Character.Pos_y
        A=self.Pos_y-target_y #gives directional vectors with Enemy at point of origin
        B=target_x-self.Pos_x
        A_neg = False
        if(A<0):    #Only dealing with directional vector above X-axis (cartesian quardinate plane with Enemy at origin)
            A_neg = True
            A = -A
        if(B!=0):
            R = A/B #Avoiding ripping a hole in the universe
            if (0<=R and R<2.4142):
                self.Direction[3]=1 #Left
            if(-2.4142<R and R<=0):
                self.Direction[1]=1 #Right
            if(R<= -0.4142 or 0.4142<=R):
                if(A_neg):
                    self.Direction[2]=1 #Up
                else:
                    self.Direction[0]=1 #Down
        elif(B==0): #Pretty much case where B approaches infinity and negative infinity
            if(A_neg):
                self.Direction[2]=1 #Up
            else:
                self.Direction[0]=1 #Down
                          
    def move(self,tick,current_level):
        current_room = current_level.get_current_room()
        
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
        if deltamove[0] !=0 or deltamove[1]!=0:
            self.setOrientation(deltamove)
        
        if deltamove[0] != 0 and deltamove[1] != 0:
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000) * 0.7
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000) * 0.7
        else:
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000)
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000)
        
        self.Pos_x,self.Pos_y = Char.Movement.tryMoveTo(self.Pos_x,self.Pos_y,
            future_Pos_x,future_Pos_y,
            self.size[0],self.size[1],
            current_level,False,self.Name)

        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.size[0],self.size[1])        
    
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

    def draw(self,tick,screen):
        drawimages = self.images
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

class Guard(Enemy):
    def __init__(self,newX,newY):
        Enemy.__init__(self,newX,newY)
        Enemy.EnemyType = 1
        self.hasGun = True
        Enemy.Hitpoints = 100
        Enemy.Armour = 1
        Enemy.AttackDamage = 2
        Enemy.SpecialTraits = 0
        self.Name = "Guard"
        self.images = [pygame.image.load('Art/Blue_hat_guard.png'),pygame.image.load('Art/Pistol.png')]
        self.currentpicture = pygame.image.load('Art/Red_Guard_Portrait.png')

class Scientist(Enemy):
    def __init__(self,newX,newY):
        Enemy.__init__(self,newX,newY)
        self.EnemyType = 2
        self.hasGun = False
        Enemy.Hitpoints = 50
        Enemy.Armour = 0
        Enemy.AttackDamage = 0
        Enemy.SpecialTraits = 0
        self.Name = "Scientist"
        self.images = [pygame.image.load('Art/Scientist.png'),pygame.image.load('Art/Arms.png')]
        self.currentpicture = pygame.image.load('Art/Green_hat_portrait.png')
        #Enemy.images = #NEED TO ADD ENEMY IMAGES#
