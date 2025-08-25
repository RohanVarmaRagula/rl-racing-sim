import pygame


global_clock = pygame.time.Clock()
WIDTH, HEIGHT = 800, 600

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def get_position(self):
        return (self.x, self.y)