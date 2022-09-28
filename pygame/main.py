import pygame
from sys import exit

#initiating pygame
pygame.init()

#creating the display surface
screen = pygame.display.set_mode((800, 400)) #contains a tuple with width and height of the game window
#changing the title of the game in the window
pygame.display.set_caption('Jump It')
clock = pygame.time.Clock()
test_surface = pygame.Surface()

while True: #keep the code running while the game isn't over
    for event in pygame.event.get(): #user interaction
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update() #update the display surface
    clock.tick(60) #the game should not run faster than 60 fps

