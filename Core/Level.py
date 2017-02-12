import pygame
import pickle
import math
class Level():

    def __init__(self):
        self.rooms = [] # [xval room, yval room, xval roomtile, yval roomtile]
        self.roomLevers = []
        self.room_grid_position = 0 # position
        self.entities = [[[] for x in range(3)] for y in range(3)] # list of entities: enemies, objects, boolets, weapons, puddings, manifestos, etc.

    def load_level(self, level_num):
        for m in range(3):
            self.rooms.append([])
            self.roomLevers.append([])
            for n in range(3):
                roomName = 'Core/Levels/' + str(level_num) + "-" + str(m) + "_" + str(n)
                self.rooms[m].append(pickle.load(open(roomName,"rb")))
                self.roomLevers[m].append(0)                

    def get_current_room(self):
        #print(len(self.rooms))
        return self.rooms[int(math.floor(self.room_grid_position/3))][self.room_grid_position%3]

    def get_current_entities(self):
        return self.entities[int(math.floor(self.room_grid_position/3))][self.room_grid_position%3]

    def enter_door(self, current_tile, character):
        if int( current_tile[0] ) == 0 and self.room_grid_position % 3 != 0:
            self.room_grid_position += -1
            character.Pos_x = 1020
        if int( current_tile[0] ) == 35 and self.room_grid_position % 3 != 2:
            self.room_grid_position += 1
            character.Pos_x = 30
        if int( current_tile[1] ) == 0 and self.room_grid_position > 2:
            self.room_grid_position += -3
            character.Pos_y = 600
        if int( current_tile[1] ) == 23 and self.room_grid_position < 6:
            self.room_grid_position += 3
            character.Pos_y = 30
            
    def activate_room_lever(self):
        self.roomLevers[int(math.floor(self.room_grid_position/3))][self.room_grid_position%3] = 1
        current_room = self.get_current_room()
        for m in range(len(current_room)):
            for n in range(len(current_room[m])):
                if current_room[m][n] == 12:
                    current_room[m][n] = 2
        
    def get_room_lever_state(self):
        return self.roomLevers[int(math.floor(self.room_grid_position/3))][self.room_grid_position%3]
