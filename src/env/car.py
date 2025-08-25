import pygame
import math
from utils import *

class Car:
    def __init__(self, image_path: str, position: Position):
       self.position = position
       self.image = pygame.image.load(image_path).convert()
       self.image = pygame.transform.scale(self.image, (75, 50))   
       self.original_image = self.image
       
       self.linear_velocity = 5
       self.rotational_velocity = 1
       self.angle = 0
       
    def set_linear_velocity(self, new_linear_velocity):
        self.linear_velocity = new_linear_velocity

    def set_rotational_velocity(self, new_rotational_velocity):
        self.rotational_velocity = new_rotational_velocity
        
    def move(self, keys_pressed):
        if keys_pressed[pygame.K_LEFT]:
            self.angle += self.rotational_velocity
        elif keys_pressed[pygame.K_RIGHT]:
            self.angle -= self.rotational_velocity
            
        if keys_pressed[pygame.K_UP]:
            self.position.x += self.linear_velocity * math.cos(math.radians(self.angle))
            self.position.y -= self.linear_velocity * math.sin(math.radians(self.angle))
        elif keys_pressed[pygame.K_DOWN]:
            self.position.x -= self.linear_velocity * math.cos(math.radians(self.angle))
            self.position.y += self.linear_velocity * math.sin(math.radians(self.angle))
            
    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        rect = rotated_image.get_rect(center=self.position.get_position())
        screen.blit(rotated_image, rect.topleft)
        
    def check_colision(self, track_mask):
        pass