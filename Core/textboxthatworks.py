import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (128,0,128)


class textbox(object):
    def __init__(self, screen):
        self.screen = screen
        self.x_pos = 36
        self.y_pos = 0
        self.x_offset = 30
        self.y_offset = 30
        self.font = pygame.font.SysFont('Calibri', 25, False, False)
        self.rendered_text = ['','','','','']
        self.text = ['','','','','']
        self.textsize = []
        self.color = [WHITE, RED, PURPLE, RED, WHITE]
        #self.x_pos += 2.5*self.x_offset #Constant offsets
        #self.y_pos += 3.5*self.y_offset        
        
    def create_textbox(self):
        pygame.draw.rect(self.screen, GREEN, [self.x_pos*self.x_offset, self.y_pos*self.y_offset, 10*self.x_offset, 24*self.y_offset]) 
        
    def line1(self):
        self.text[0] = "Test1"
        self.rendered_text[0] = self.font.render(str(self.text[0]), True, BLACK)
    
    def line2(self):
        self.text[1] = "Test2"
        self.rendered_text[1] = self.font.render(str(self.text[1]), True, BLACK)
        
    def line3(self):
        self.text[2] = "Test3"
        self.rendered_text[2] = self.font.render(str(self.text[2]), True, BLACK)
        
    def line4(self):
        self.text[3] = "Test4"
        self.rendered_text[3] = self.font.render(str(self.text[3]), True, BLACK)
        
    def line5(self):
        self.text[4] = "Test5"
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
                boxrect = pygame.Rect([((self.x_pos*self.x_offset)+self.x_gap)- (1/2)*self.textsize[i][0], ((self.y_pos*self.y_offset)+self.y_gap)-(1/2)*self.textsize[i][1], 2*self.textsize[i][0], 2*self.textsize[i][1]])
                pygame.draw.rect(self.screen, self.color[i], boxrect)
                #Do blit after!
                self.screen.blit(self.rendered_text[i], [((self.x_pos*self.x_offset)+self.x_gap), ((self.y_pos*self.y_offset)+ self.y_gap)])
            self.y_gap += 4*self.y_offset
            #Probably bigger offset than 2, and prob x offset as well (5 ish)
            #draw a rect around the words after for buttons
            
    def callbacks(self, click_pos):
        print( click_pos )
        for i in range (len(self.rendered_text)): #have to def 5 lines to work
            boxrect = pygame.Rect([((self.x_pos*self.x_offset)+self.x_gap)- (1/2)*self.textsize[i][0], ((self.y_pos*self.y_offset)+self.y_gap)-(1/2)*self.textsize[i][1], 2*self.textsize[i][0], 2*self.textsize[i][1]])
            if boxrect.collidepoint(click_pos):
                return i
            else:
                return "none"
                
                
    def txt_getcmd(self, command):
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
