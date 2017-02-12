

def lineOfSight(self, target, current_level):
    f_x = self.Pos_x + self.size[0]/2
    f_y = self.Pos_y + self.size[1]/2
    t_x =target.Pos_x+target.size[0]/2
    t_y =target.Pos_y+target.size[1]/2
    dx = (t_x - f_x) / 100
    dy = (t_y - f_y) / 100
    if abs(dx) > abs(dy):
        if dx > 0 and dy > 0:
            ors = [1,2]
        elif dx > 0 and dy <= 0:
            ors = [2,3]
        elif dx <= 0 and dy > 0:
            ors = [6,7]
        else:# dx <= 0 and dy <= 0:
            ors = [5,6]
    else: #abs(dx) <= abs(dy):
        if dx > 0 and dy > 0:
            ors = [0,1]
        elif dx > 0 and dy <= 0:
            ors = [3,4]
        elif dx <= 0 and dy > 0:
            ors = [7,0]
        else:# dx <= 0 and dy <= 0:
            ors = [4,5]
    if self.Orientation not in ors:
        return False
    
    current_room = current_level.get_current_room()
    
    for i in range(101):
        b_x = self.Pos_x + i*dx
        b_y = self.Pos_y + i*dy
        gridpos_x = int((b_x)//30)
        gridpos_y = int((b_y)//30)
        if ( int( current_room[gridpos_x][gridpos_y] ) in (-1, 1, 2, 4, 9, 12, 13, 14, 15, 20, 21, 22)):
            return False
        return True
