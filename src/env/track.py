import pygame 
from utils import *

class Track:
    
    def __init__(self, image_path: str):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))
        
    def get_mask(self):
        pass