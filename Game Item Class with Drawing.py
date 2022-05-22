import pygame
from pygame.locals import *
from sys import exit


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))  # 设置显示屏幕返回为surface对象
    pygame.display.set_caption('draw')  # 设置标题
    pygame.display.set_icon(pygame.image.load('img/boom/boom01.png'))  # 设置标题的图标
    while True:
        for event in pygame.event.get():  # pygame.event.get()返回Eventlist列表
            if event.type == pygame.QUIT:  #
                pygame.quit()  # 退出pygame
                exit()  # 退出python解释器
        pygame.draw.aaline(screen, (255, 255, 255), (20, 20), (100, 100))  # draw模块的aaline方法
        pygame.display.update()  # 刷新


if __name__ == '__main__':
    main()
