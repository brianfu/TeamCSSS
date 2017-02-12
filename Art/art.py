import pygame
import os

class art(object):
    
    def __init__(self, screen):
        self.pic_names = []
        self.screen = screen
        for i in os.listdir(path="./Art"):
            if (".png" or ".jpg") in i:
                self.pic_names.append(i)
        self.ready_img = []
        self.picname_noext = []
        os.chdir("./Art")
        for i in range (len(self.pic_names)):
            self.ready_img.append(pygame.image.load(str(self.pic_names[i])).convert())
            self.picname_noext.append(str(self.pic_names[i]))
        #for i in range (len(self.picname_noext)):
    
    def blitz(self, picture_no, x, y):
        self.img_index = self.picname_noext.index(str(picture_no))
        self.screen.blit(self.ready_img[self.img_index], [x,y])
                
                
                                
            
            
            
'''
            def blitz(self,x,y):
                self.pic_iter
                
            
            def blitz(self,x,y):
                art.screen.blit(art.pic_names[i],x,y)
#a = Art.art(screen)
#Art.art.(picnamew/oext)()
#a.(picnamew/oext).blitz(x,y)
'''
        
    
            
    
    