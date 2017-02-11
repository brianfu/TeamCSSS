import pygame
from pygame.locals import *
class Command(object):
    
    def __init__(self):
        self.ctype = "null" #types are go_dir stop_dir ghost_mode etc
        self.spec = "null" #UP,DOWN,LEFT,RIGHT,true, false
        self.commands = {
            pygame.K_w: 2,
            pygame.K_d: 1,
            pygame.K_a: 3,
            pygame.K_s: 0
            }
        
    def makeFromEvent(self,event): #makes the command from an event, to be passed to an object
        if event.type == KEYDOWN and event.key == K_SPACE:
            self.ctype = "ghost_mode"
            self.spec = "swap"
            return 0;
        if event.type == KEYDOWN:
            self.ctype = "go_dir";
            if event.key in self.commands.keys():
                self.spec = self.commands[event.key];
            else: self.spec = "null";
        
        elif event.type == KEYUP:
            self.ctype = "stop_dir";
            if event.key in self.commands.keys():
                self.spec = self.commands[event.key];
            else: self.spec = "null";
            
            
