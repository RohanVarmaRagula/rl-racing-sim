import pygame
from utils import *
from car import Car
from track import Track

class racing_env:
    
    def __init__(self, car_image: str, track_image: str):
        pygame.init()
        pygame.display.set_caption("rl-racing-simulator")
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.car = Car(car_image, Position(200, 25))
        self.track = Track(track_image)
        
    def render(self):
        
        running = True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                keys_pressed = pygame.key.get_pressed()
                self.car.move(keys_pressed)
            
            self.screen.blit(self.track.image, (0, 0))
            self.car.move(keys_pressed)
            self.car.draw(self.screen)
            
            pygame.display.flip()
            
        pygame.quit()
        
        
if __name__ == "__main__":
    env = racing_env(car_image="assets/cars/white_car.png",
                     track_image="assets/tracks/oval.png")
    env.render()    