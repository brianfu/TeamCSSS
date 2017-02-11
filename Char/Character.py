

class Character(object):
    
    def __init__(self):
        self.Ghoststate = false
        self.Pos.x = 50;
        self.Pos.y = 50;
        self.Timecountdown = 200 #at 60fps, the number should be 60*time wanted
        #self.Direction = 0; #can be 0-7, 
        self.Orientation = 0; #can be 0-3
        self.Velocity = 216 #pixels / second
        self.Direction = [0,0,0,0]
        
    def update(self,tick):
        deltamove = [0,0];
        for i in range(4):
            if i==3 or i==4:
                deltamove[i%2] += self.Direction[i]* -1;
            else:
                deltamove[i%2] += self.Direction[i]; #add 1 to deltamove if 0 or 1, minus 1 if 2 or 3
        
        if deltamove[0] != 0 and deltamove[1] != 0:
            self.Pos.x += deltamove[0]*(self.Velocity*tick/1000) * 0.7
            self.Pos.y += deltamove[1]*(self.Velocity*tick/1000) * 0.7
        else:
            self.Pos.x += deltamove[0]*(self.Velocity*tick/1000) 
            self.Pos.y += deltamove[1]*(self.Velocity*tick/1000)            
        
        
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
    
            
    def draw(self,screen):
        return 0; #Update later with drawing stuff