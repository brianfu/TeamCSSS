from . import soundlib

def update(char,tick):
    if char.PlayGhostSound:
        soundlib.play_sound("ghostdimentioncountdownEnding.wav")
        char.PlayGhostSound = False