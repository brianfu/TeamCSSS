import pygame
from pygame.locals import *
class Command(object):
    
    def __init__(self):
        self.ctype = "null" #types can be keypress, keydepress, or other things for other objects
        self.spec = "null" #UP,DOWN,LEFT,RIGHT, etc
        self.commands = {
            pygame.K_w: "UP",
            pygame.K_d: "RIGHT",
            pygame.K_a: "LEFT",
            pygame.K_s: "DOWN"
            }
        
    def makeFromEvent(self,event): #makes the command from an event, to be passed to an object
        if event.type == KEYDOWN:
            self.ctype = "keypress";
            if event.key in self.commands.keys():
                self.spec = self.commands[event.key];
            else: self.spec = "null";
        
        elif event.type == KEYUP:
            self.ctype = "keydepress";
            if event.key in self.commands.keys():
                self.spec = self.commands[event.key];
            else: self.spec = "null";
            
            
