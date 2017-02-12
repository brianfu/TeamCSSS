import pygame
import math
class Bullet():

    def __init__(self, origin_x, origin_y, aim_x, aim_y):
        self.Pos_x = origin_x
        self.Pos_y = origin_y
        self.Origin_x = origin_x
        self.Origin_y = origin_y
        self.Aim_x = aim_x
        self.Aim_y = aim_y
        self.rect = pygame.Rect(self.Pos_x,self.Pos_y,self.Pos_x+1,self.Pos_x+1)
        self.speed = 30
        self.m = (Aim_y - Origin_y)/(Aim_x - Origin_x)

    def update(self,tick,current_room,enemylist,char):
        self.move(tick,current_room)

    def get_y(self,x):
        y = self.m*(x - Origin_x) + Origin_y
        return x

    def get_x(self,y):
        x = (1/self.m)*(y - Origin_y) + Origin_x
        return y

    def move(self,tick,current_room):
        if m > 0:
            print("test")
