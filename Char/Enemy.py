import pygame
import os

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
<<<<<<< HEAD
        self.Pos_x = newX;
        self.Pos_y = newY;
        self.EnemyType = 0
=======
        self.Possessable = True
        self.Pos_x = 50;
        self.Pos_y = 50;
        self.EnemyType = 0 
>>>>>>> a85fcbb61d3c89f8e3626dff6920e531f1da9e34
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


    def update(self,tick):
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
            self.Pos_x += deltamove[1]*(self.Velocity*tick/1000)
            self.Pos_y += deltamove[0]*(self.Velocity*tick/1000)
            future_Pos_x += deltamove[1]*(self.Velocity*tick/1000)
            future_Pos_y += deltamove[0]*(self.Velocity*tick/1000)
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
