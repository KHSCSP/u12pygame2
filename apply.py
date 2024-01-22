import pygame, sys
from pygame.locals import QUIT

pygame.init()
w = 400
h = 300
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

# define your functions in a different file
# call your functions here

                                 
pygame.display.update()                                 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


