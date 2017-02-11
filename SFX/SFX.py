# Hey Hey, it was past 4:00 AM when I last touched this file, forgive me for any and all mistakes -Toshi
class SFX(object):
    def __init__(self, characterList):
        pygame.mixer.init()
        self.prevChars = characterList
        self.SFXslowFootStep1 = pygame.mixer.Sound("slowfootsteps1version1.wav")
        self.SFXslowFootStep2 = pygame.mixer.Sound("slowfootsteps1version2.wav")
        
    def sfxcall(currentChars):
        for oldChar in self.prevChars: # Foot Steps
            for newChar in currentChars:
                if oldChar[0] != newChar[0]: #if old x, y is not equal to new x, y
                    if abs( oldChar[0] - newChar[0] ) < 2: #temp number, basically to tell apart slow stroll from fast walk
                        if random.randrange(1,6) == 1:
                            self.SFXslowFootStep1.play()
                        else:
                            self.SFXslowFootStep2.play()
                elif oldChar[1] != newChar[1]: #if old x, y is not equal to new x, y
                    if abs( oldChar[1] - newChar[1] ) < 2: #temp number, basically to tell apart slow stroll from fast walk
                        if random.randrange(1,6) == 1:
                            self.SFXslowFootStep1.play()
                        else:
                            self.SFXslowFootStep2.play()
