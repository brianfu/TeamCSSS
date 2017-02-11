import pygame

def detect_collision(rect1, rect2):
    if rect1.colliderect(rect2):
        return 1
    else:
        return 0
