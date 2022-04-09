import pygame,sys

pygame.init()
size = width, height = 600, 400
speed1 = [1, 1]
speed2 = [2, 2]
BLACK = 0, 0, 0
s = pygame.display.set_mode(size)
pygame.display.set_caption("ball speed")
ball1 = pygame.image.load(r'D:\Users\熊政\PycharmProjects\pythonProject\PYG02-ball.gif')
ball2 = pygame.image.load(r'D:\Users\熊政\PycharmProjects\pythonProject\PYG02-ball.gif')
ball1rect = ball1.get_rect()
ball2rect = ball1.get_rect()
fps = 200
fclock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ball1rect = ball1rect.move(speed1[0], speed1[1])
    if ball1rect.left < 0 or ball1rect.right > width:
        speed1[0] = - speed1[0]
    if ball1rect.top < 0 or ball1rect.bottom > height:
        speed1[1] = - speed1[1]
    ball2rect = ball2rect.move(speed2[0], speed2[1])
    if ball2rect.left < 0 or ball2rect.right > width:
        speed2[0] = - speed2[0]
    if ball2rect.top < 0 or ball2rect.bottom > height:
        speed2[1] = - speed2[1]

    s.fill(BLACK)
    s.blit(ball1, ball1rect)
    s.blit(ball2, ball2rect)
    pygame.display.update()
    fclock.tick(fps)