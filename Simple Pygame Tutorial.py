import pygame;
import sys;
import os;
import math;

dirname, runFile = os.path.split(os.path.abspath(sys.argv[0]));

pygame.init();
pygame.display.set_caption("Pong")
size = width, height = 800, 600;

# 显示窗口
scene = pygame.display.set_mode(size);
bgColor = (0, 0, 0);


ball = pygame.image.load(dirname + r'D:\Users\熊政\PycharmProjects');
ballRect = ball.get_rect();


leftBlock = pygame.image.load(dirname + '/img/block.jpg');
leftBlockRect = leftBlock.get_rect();
leftBlockRect.centerx = 40;
leftBlockRect.centery = 300;


rightBlock = pygame.image.load(dirname + '/img/block.jpg');
rightBlockRect = rightBlock.get_rect();
rightBlockRect.centerx = 760;
rightBlockRect.centery = 300;



def drawLine():
    lineColor = (255, 255, 255);
    for i in range(0, 40):
        start = (400, i * 15);
        end = (400, i * 15 + 10);
        pygame.draw.line(scene, lineColor, start, end, 4);



leftScoreNum = 0;
rightScoreNum = 0;


def leftScoreShow():
    font = pygame.font.Font(None, 100);
    leftScore = font.render(str(leftScoreNum), 1, (255, 255, 255));
    leftScoreRect = leftScore.get_rect();
    leftScoreRect.centerx = 200;
    leftScoreRect.centery = 70;
    scene.blit(leftScore, leftScoreRect);

# 右侧分数
def rightScoreShow():
    font = pygame.font.Font(None, 100);
    rightScore = font.render(str(rightScoreNum), 1, (255, 255, 255));
    rightScoreRect = rightScore.get_rect();
    rightScoreRect.centerx = 600;
    rightScoreRect.centery = 70;
    scene.blit(rightScore, rightScoreRect);


# 得分
def addScore(type):
    if type == 1 :
        global leftScoreNum;
        leftScoreNum = leftScoreNum + 1;

    else :
        global rightScoreNum;
        rightScoreNum = rightScoreNum + 1;


# 重置小球
def resetBall(type):
    global ballRect;
    global ballSpeedAngle;
    ballRect.centerx = 400;
    ballRect.centery = 300;

    if type == 1 :
        ballSpeedAngle = 0;

    else :
        ballSpeedAngle = math.pi;


# 挡板与球的碰撞
isLeftBlockCrash = False;
isRightBlockCrash = False;
def blockCrash(speedX):
    global isLeftBlockCrash;
    global isRightBlockCrash;
    global ballSpeedAngle;
    if (ballRect.centerx < leftBlockRect.centerx + leftBlockRect.width / 2 and ballRect.centerx > leftBlockRect.centerx - leftBlockRect.width / 2) and (ballRect.centery < leftBlockRect.centery + leftBlockRect.height / 2 and ballRect.centery > leftBlockRect.centery - leftBlockRect.height / 2) :
        if isLeftBlockCrash == False :
            if speedX > 0 :
                ballSpeedAngle = -(ballSpeedAngle - math.pi);

            else :

                ballSpeedAngle = (ballRect.centery - leftBlockRect.centery)/50;

            isLeftBlockCrash = True;

    else :
        isLeftBlockCrash = False;


    if (ballRect.centerx < rightBlockRect.centerx + rightBlockRect.width / 2 and ballRect.centerx > rightBlockRect.centerx - rightBlockRect.width / 2) and (ballRect.centery < rightBlockRect.centery + rightBlockRect.height / 2 and ballRect.centery > rightBlockRect.centery - rightBlockRect.height / 2) :
        if isRightBlockCrash == False :
            if speedX > 0 :
                ballSpeedAngle = -(ballSpeedAngle - math.pi);

            else :

                ballSpeedAngle = (ballRect.centery - rightBlockRect.centery)/50;

            isRightBlockCrash = True;

    else :
        isRightBlockCrash = False;



fpsClock = pygame.time.Clock();


ballSpeed = 15;

ballSpeedAngle = 1/4 * math.pi;


leftMoveSpeed = 0;
rightMoveSpeed = 0;





while True:


    speedX = math.cos(ballSpeedAngle) * ballSpeed;
    speedY = math.sin(ballSpeedAngle) * ballSpeed;


    ballRect.centerx += speedX;
    ballRect.centery += speedY;


    leftBlockRect.centery += leftMoveSpeed;
    if(leftBlockRect.centery < 50):
        leftBlockRect.centery = 50;

    if(leftBlockRect.centery > 550):
        leftBlockRect.centery = 550;


    rightBlockRect.centery += rightMoveSpeed;
    if(rightBlockRect.centery < 50):
       rightBlockRect.centery = 50;

    if(rightBlockRect.centery > 550):
        rightBlockRect.centery = 550;



    if(ballRect.centery > 600):
        ballSpeedAngle = -ballSpeedAngle;

    if(ballRect.centery < 0):
        ballSpeedAngle = -ballSpeedAngle;

    if(ballRect.centerx > 800):
        ballSpeedAngle = -(ballSpeedAngle - math.pi);
        addScore(1);
        resetBall(1);

    if(ballRect.centerx < 0):
        ballSpeedAngle = -(ballSpeedAngle - math.pi);
        addScore(0);
        resetBall(0);


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rightMoveSpeed = -8;

            if event.key == pygame.K_DOWN:
                rightMoveSpeed = 8;

            if event.key == pygame.K_w:
                leftMoveSpeed = -8;

            if event.key == pygame.K_s:
                leftMoveSpeed = 8;


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                rightMoveSpeed = 0;

            if event.key == pygame.K_DOWN:
                rightMoveSpeed = 0;

            if event.key == pygame.K_w:
                leftMoveSpeed = 0;

            if event.key == pygame.K_s:
                leftMoveSpeed = 0;



    scene.fill(bgColor);
    scene.blit(ball, ballRect);
    scene.blit(leftBlock, leftBlockRect);
    scene.blit(rightBlock, rightBlockRect);
    drawLine();   # Draw a dotted center line
    leftScoreShow(); # Left side score display
    rightScoreShow(); # right side score display

    blockCrash(speedX); # Collision detection
    pygame.display.update();  # Update all display

    fpsClock.tick(30);  # Set the interval of the PyGame clock