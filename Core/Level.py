import pygame
import pickle
import math
class Level():

    def __init__(self):
        self.rooms = [] # [xval room, yval room, xval roomtile, yval roomtile]
        self.room_grid_position = 2 # position
        self.entities = [[[]]] # list of entities: enemies, objects, boolets, weapons, puddings, manifestos, etc.

    def load_level(self, level_num):
        for m in range(3):
            self.rooms.append([])
            for n in range(3):
                roomName = 'Core/' + str(level_num) + "-" + str(m) + "_" + str(n)
                self.rooms[m].append(pickle.load(open(roomName,"rb")))

    def get_current_room(self):
        print(len(self.rooms))
        return self.rooms[int(math.floor(self.room_grid_position/3))][self.room_grid_position%3]

    def get_current_entities(self):
        return self.entities[int(math.floor(self.room_grid_position/3))][self.room_grid_position%3]

    def enter_door(self, current_tile, character):
        if current_tile[0] == 0 and self.room_grid_position % 3 != 0:
            self.room_grid_position += -1
            character.Pos_x = 1020
        if current_tile[0] == 35 and self.room_grid_position % 3 != 2:
            self.room_grid_position += 1
            character.Pos_x = 30
        if current_tile[1] == 0 and self.room_grid_position > 2:
            self.room_grid_position += -3
            character.Pos_y = 600
        if current_tile[1] == 23 and self.room_grid_position < 6:
            self.room_grid_position += 3
            character.Pos_y = 30
