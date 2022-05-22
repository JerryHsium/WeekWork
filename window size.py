import pygame
from pygame.locals import *
pygame.init()  # Initial
screen = pygame.display.set_mode((800,600))  # make a window
pygame.display.set_caption("game")  # name
keep_going = True  # Circulation
BLACK = (0, 0, 0) # black

while keep_going:
    for event in pygame.event.get():
        if event.type == QUIT:
            keep_going = False
    screen.fill(BLACK) # block

pygame.quit()