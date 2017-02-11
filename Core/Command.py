class Command(object):
    
    def __init__(self):
        self.ctype = "null" #types can be keypress, keydepress, or other things for other objects
        self.spec = "null" #UP,DOWN,LEFT,RIGHT, etc
        self.commands = {
            K_UP: "UP",
            K_RIGHT: "RIGHT",
            K_LEFT: "LEFT",
            K_DOWN: "DOWN"
            }
        
    def makeFromEvent(self,event): #makes the command from an event, to be passed to an object
        if event.type == KEYDOWN:
            self.ctype = "keypress";
            if event.key in self.commands.keys():
                self.spec = self.commands[event.type];
            else: self.spec = "null"
        
        elif event.type == KEYUP:
            self.ctype = "keydepress";
            if event.key in self.commands.keys():
                self.spec = self.commands[event.type];
            else: self.spec = "null";            
            