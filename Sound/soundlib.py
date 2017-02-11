import pygame
import os

MUSIC_PATH = "Music"
SFX_PATH = "SFX"

_sfx_lib = { }

def play_music(filename, timesToPlay=1):
        """Plays the music specified by filename. 
        timesToPlay is the number of times the music will play (Default is 1). 
        A value of 0 or -1 will loop the music infinitely until stop_music is called"""
        
        # Check if any music is playing, stop it if it is
        if pygame.mixer.music.get_busy():
                pygame.mixer.music.fadeout(1000)
        
        # Get rid of trailing/beginning whitespaces
        if filename.strip() == "":
                return
        
        # Correct timesToPlay, because PyGame weirdness
        if timesToPlay > -1:
                timesToPlay = timesToPlay-1
        elif timesToPlay < -1:
                timesToPlay = -1
        
        # Make the filepath all proper-like and canonicalized
        filepath = "{}/{}".format(MUSIC_PATH, filename)
        canonicalized_filepath = filepath.replace('/', os.sep).replace('\\', os.sep)
        
        # Load and Play the music
        pygame.mixer.music.load(canonicalized_filepath)
        pygame.mixer.music.play(timesToPlay)
        
def stop_music(abrupt=False):
        """Stops whatever music is playing"""
        
        # If nothing is playing, return
        if not pygame.mixer.music.get_busy():
                return
        
        # Either abruptly stop, or fade out over a second
        if abrupt:
                pygame.mixer.music.stop()
        else:
                pygame.mixer.music.fadeout(1000)
                
def play_sound(filename):
        """Plays the sound specified by filename"""
        
        # Grab our global sfx dictionary
        global _sfx_lib
        
        # Format our filepath
        filepath = "{}/{}".format(SFX_PATH, filename)
        
        # Grab our sound from the dictionary if it's already instantiated
        sound = _sfx_lib.get(filepath)
        
        # If it isn't instantiated, instantiate it
        if sound == None:
                # Canonicalize the filepath
                canonicalized_filepath = filepath.replace('/', os.sep).replace('\\', os.sep)
                # Instantiate the sound
                sound = pygame.mixer.Sound(file=canonicalized_filepath)
                # Save our loaded sound for later
                _sfx_lib[filepath] = sound
        
        #Play the sound
        sound.play()