import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class textbox(object):
    def __init__(self, screen):
        self.screen = screen
        self.x_pos = 0
        self.y_pos = 19
        self.x_offset = 30
        self.y_offset = 30
        self.font = pygame.font.SysFont('Calibri', 25, False, False)
        self.rendered_text = ['','','','','']
        
    def create_textbox(self):
        pygame.draw.rect(self.screen, RED, [self.x_pos*self.x_offset, self.y_pos*self.y_offset, 36*self.x_offset, 5*self.y_offset]) 
        
    def line1(self, text):
        self.rendered_text[0] = self.font.render(str(text), True, BLACK)
    
    def line2(self, text):
        self.rendered_text[1] = self.font.render(str(text), True, BLACK)
        
    def line3(self, text):
        self.rendered_text[2] = self.font.render(str(text), True, BLACK)
        
    def line4(self, text):
        self.rendered_text[3] = self.font.render(str(text), True, BLACK)
        
    def line5(self, text):
        self.rendered_text[4] = self.font.render(str(text), True, BLACK)
    
    def blitz(self):
        for i in range (len(self.rendered_text)): #have to def 5 lines to work
            if isinstance(self.rendered_text[i], str):
                pass
            else:
                self.screen.blit(self.rendered_text[i], [self.x_pos*self.x_offset, self.y_pos*self.y_offset])
            self.y_pos += 1
        