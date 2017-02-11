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

class Character(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.Possesedstate = false
        self.Pos.x = 50;
        self.Pos.y = 50;
        self.EnemyType = 0 #Enemy Type should be stored as integer, which should lead to an entry in a list with appropriate Hitpoints/Amrour/AttackDamage/SpecialTraits values.
        self.Hitpoints = 100
        self.Armour = 0
        self.AttackDamage = 0
        self.SpecialTraits = 0 #Special Traits are stored as integers and checked for as integers.
        #self.Direction = 0; #can be 0-7, 
        self.Orientation = 0 #can be 0-3
        self.Velocity = 216 #pixels / second
        self.Direction = [0,0,0,0]
        self.images = [pygame.image.load('Art/Char_0.jpg'),pygame.image.load('Art/Char_1.png')]
        
        
    def update(self,tick):
        deltamove = [0,0];
        for i in range(4):
            if i==3 or i==2:
                deltamove[i%2] += self.Direction[i]* -1;
            else:
                deltamove[i%2] += self.Direction[i]; #add 1 to deltamove if 0 or 1, minus 1 if 2 or 3
        
        if deltamove[0] != 0 and deltamove[1] != 0:
            self.Pos_x += deltamove[1]*(self.Velocity*tick/1000) * 0.7
            self.Pos_y += deltamove[0]*(self.Velocity*tick/1000) * 0.7
        else:
            self.Pos_x += deltamove[1]*(self.Velocity*tick/1000) 
            self.Pos_y += deltamove[0]*(self.Velocity*tick/1000)
        if self.Ghoststate:
            self.image = self.images[1];
        else: self.image = self.images[0];
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
            elif command.spec == "DIMENSION":
                self.Ghoststate = not self.Ghoststate
        elif command.ctype == "keydepress":
            if command.spec == "DOWN":
                self.Direction[0] = 0;
            elif command.spec == "RIGHT":
                self.Direction[1] = 0;
            elif command.spec == "UP":
                self.Direction[2] = 0;
            elif command.spec == "LEFT":
                self.Direction[3] = 0;            
        
'''
    def draw(self,screen):
        self.image.draw(screen);
        return 0; #Update later with drawing stuff'''
