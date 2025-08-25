# <a href"https://www.flaticon.com/free-icons/car" title="car icons">Car icons created by Smashicons - Flaticon</a>

import pygame

pygame.init()

screen = pygame.display.set_mode((888,666))
pygame.display.set_caption('Gamezone')

img = pygame.image.load('../assets/racing-car.png')
pygame.display.set_icon(img)

clock = pygame.time.Clock()

isRunning=True
screen.fill((10, 10, 100))  # navy blue background
pygame.display.flip() # helps swap back buffer with screen
clock.tick(60) # set to 60 fps for now

while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning= not isRunning

pygame.quit()

# print("pygame installed successfully")