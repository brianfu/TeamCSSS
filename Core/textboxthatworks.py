import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128,0,128)
GREY = (220,220,220)

#Shadow bar
#Controls
#Portriat
#Health

class textbox(object):
    def __init__(self, screen):
        self.screen = screen
        self.x_pos = 36
        self.y_pos = 0
        self.x_offset = 30
        self.y_offset = 30
        self.font = pygame.font.SysFont('Arial', 12,True, False)
        self.rendered_text = ['','','','','']
        self.text = ['','','','','']
        self.textsize = []
        self.color = [WHITE, RED, PURPLE, RED, WHITE]
        self.rec_area_mat = []
        self.mouse_pos = pygame.mouse.get_pos()
        self.draw_border = 2
        self.shadow_percentage = 0.50 #between 0 and 1
        
        #init text declares
        for i in range (5):
            self.text[i] = "Test" + str(i)
        
        #Trigger Booleans
        self.mBdown = False        
        #self.x_pos += 2.5*self.x_offset #Constant offsets
        #self.y_pos += 3.5*self.y_offset
       
    ''' 
    def shadow_bar(self, shadow_remaining):
        pygame.draw.rect(self.screen, GREY, [918, 120, 4*30, 30], 2)
        pygame.draw.rect(self.screen, GREY, [918, 120, 4*30 - shadow_remaining, 30])
    '''
        
    def create_textbox(self):
        pygame.draw.rect(self.screen, BLACK, [self.x_pos*self.x_offset, self.y_pos*self.y_offset, 10*self.x_offset, 24*self.y_offset]) 
        
    def line1(self):
        self.rendered_text[0] = self.font.render(str(self.text[0]), True, GREY)
    
    def line2(self):
        self.rendered_text[1] = self.font.render(str(self.text[1]), True, BLACK)
        
    def line3(self):
        self.rendered_text[2] = self.font.render(str(self.text[2]), True, BLACK)
        
    def line4(self):
        self.rendered_text[3] = self.font.render(str(self.text[3]), True, BLACK)
        
    def line5(self):
        self.rendered_text[4] = self.font.render(str(self.text[4]), True, BLACK)
    
    def blitz(self):
        self.y_gap = 0
        self.x_gap = 0
        self.textsize = []
        self.x_gap += 2.5*self.x_offset
        self.y_gap += 3*self.y_offset
        for i in range (len(self.rendered_text)): #have to def 5 lines to work
            if isinstance(self.rendered_text[i], str):
                pass
            else:
                self.textsize.append(self.font.size(self.text[i]))
                '''
                boxrect = pygame.Rect([((self.x_pos*self.x_offset)+self.x_gap)- (1/2)*self.textsize[i][0], ((self.y_pos*self.y_offset)+self.y_gap)-(1/2)*self.textsize[i][1], 2*self.textsize[i][0], 2*self.textsize[i][1]])
                pygame.draw.rect(self.screen, self.color[i], boxrect)
                '''
                #temp declares for mat
                x_temp = ((self.x_pos*self.x_offset)+self.x_gap)- (1/3)*self.textsize[i][0]
                y_temp = ((self.y_pos*self.y_offset)+self.y_gap)- (1/2)*self.textsize[i][1]
                width_temp = self.textsize[i][0] + 20
                height_temp = self.textsize[i][1] + 20
                final_mat_temp = [x_temp -10, y_temp -10, width_temp, height_temp]
                
                #draw dynamic box
                if i == 0: #For shadow
                    final_mat_temp[2] *= self.shadow_percentage
                    pygame.draw.rect(self.screen, PURPLE, final_mat_temp)
                    final_mat_temp[2] /= self.shadow_percentage
                    pygame.draw.rect(self.screen, self.color[i], final_mat_temp, self.draw_border)
                else:
                    pygame.draw.rect(self.screen, self.color[i], final_mat_temp)
                
                #get rect values here, put into 5 x 4 mat, call by seeing if mouse pos in that area and if something pressed
                
                #if list in matrix, pass, else add to mat
                if final_mat_temp not in self.rec_area_mat:
                    self.rec_area_mat.append(final_mat_temp) 
                    
                #Do blit after!
                self.screen.blit(self.rendered_text[i], [x_temp, y_temp])
            self.y_gap += 4*self.y_offset
            #Probably bigger offset than 2, and prob x offset as well (5 ish)
            #draw a rect around the words after for buttons
            
            '''
    def callbacks(self, click_pos):
        #print( click_pos )
        for i in range (len(self.rendered_text)): #have to def 5 lines to work
            boxrect = pygame.Rect([((self.x_pos*self.x_offset)+self.x_gap)- (1/2)*self.textsize[i][0], ((self.y_pos*self.y_offset)+self.y_gap)-(1/2)*self.textsize[i][1], 2*self.textsize[i][0], 2*self.textsize[i][1]])
            if boxrect.collidepoint(click_pos[0], click_pos[1]):
                return i
            else:
                return "none"
            '''
    
    def button_trigger(self): #call this after blitz for button func, must be called after!
        #Also call after line render methods so that vars are blitted properly
        self.mouse_pos = pygame.mouse.get_pos()
        self.button = [] #reset so no infinite list
        
        #bounds declare
        for i in range(len(self.rec_area_mat)):
            rounded_x = round(self.rec_area_mat[i][0])
            rounded_x_0 = round(self.rec_area_mat[i][0]+self.rec_area_mat[i][2])
            rounded_y = round(self.rec_area_mat[i][1])
            rounded_y_0 = round(self.rec_area_mat[i][1]+self.rec_area_mat[i][3])
            if self.mBdown and self.mouse_pos[0] in range (rounded_x,rounded_x_0+1) and self.mouse_pos[1] in range (rounded_y, rounded_y_0 + 1): #if mBdown trigger and in range between x and x(not) and y and y(not)
                self.button.append(True)
            else:
                self.button.append(False)
                    
        #Button actions
        if self.button[0]: #only 1 button press at a time
            pass
        elif self.button[1]:
            self.text[1] = "Hint: 'W' is UP!"
        elif self.button[2]:
            pass
        elif self.button[3]:
            pass
        elif self.button[4]:
            pass

                
                
    def txt_getcmd(self, command):
        self.mBdown = False
        if command.ctype == "go_dir":
            if command.spec == 2:
                pass #forward, 'w'
            elif command.spec == 0:
                pass #down
            elif command.spec == 1:
                pass #right
            elif command.spec == 3:
                pass #left
        elif command.ctype == "stop_dir":
            pass #keyup
        elif command.ctype == "fire_gun":
            self.mBdown = True
            pass #mbdown
        elif command.ctype == "non_firing":
            pass #mbup    
'''
    textbox = Core.textboxthatworks.textbox(screen)
    textbox.line1()
    textbox.line2()
    textbox.line3()
    textbox.line4()
    textbox.line5()
    textbox.create_textbox()
    textbox.blitz()    
'''
