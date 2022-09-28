import pygame

#initiating pygame
pygame.init()

#creating the display surface
screen = pygame.display.set_mode((800, 400)) #contains a tuple with width and height of the game window

while True: #keep the code running while the game isn't over
    pygame.display.update() #update the display surface
