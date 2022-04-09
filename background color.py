import pygame,sys

pygame.init()

size = width, height = 600, 400
WHITE = 250, 250, 250
screen = pygame.display.set_mode(size)
pygame.display.set_caption("background color")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    pygame.display.update()