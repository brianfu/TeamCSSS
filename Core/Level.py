import pygame
import pickle
class Level():

    def __init__(self):
        self.rooms = [] # [xval room, yval room, xval roomtile, yval roomtile]
        self.room_grid_position = [0,0] # x value, y value
        self.entities = [] # list of entities: enemies, objects, weapons, puddings, manifestos, etc.

    def load_level(self, level_num):
        for m in range(3 - 1):
            self.rooms.append([])
            for n in range(3 - 1):
                roomName = 'Core/' + str(level_num) + "-" + str(m) + "_" + str(n)
                self.rooms[m].append(pickle.load(open(roomName,"rb")))

    def get_current_room(self):
        return self.rooms[self.room_grid_position[0]][self.room_grid_position[1]]

    def enter_door(current_tile):
        if current_tile[0] == 0 and room_grid_position[0] != 0:
            self.room_grid_position[0] += -1
        if current_tile[0] == 35 and room_grid_position[0] != 2:
            self.room_grid_position[0] += 1
        if current_tile[1] == 0 and room_grid_position[1] != 0:
            self.room_grid_position[1] += -1
        if current_tile[1] == 23 and room_grid_position[1] != 2:
            self.room_grid_position[1] += 1
