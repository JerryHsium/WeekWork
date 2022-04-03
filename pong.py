import pygame;
import sys;
import os;
import math;

dirname, runFile = os.path.split(os.path.abspath(sys.argv[0]));

pygame.init();  # 初始化pygame
pygame.display.set_caption("Pong") # 设置标题
size = width, height = 800, 600;  # 设置窗口大小

# 显示窗口
scene = pygame.display.set_mode(size);
bgColor = (0, 0, 0);  # 设置颜色

# 添加小球图片
ball = pygame.image.load(dirname + '/img/ball.jpg');
ballRect = ball.get_rect();

# 添加左挡板图片
leftBlock = pygame.image.load(dirname + '/img/block.jpg');
leftBlockRect = leftBlock.get_rect();
leftBlockRect.centerx = 40;
leftBlockRect.centery = 300;

# 添加右挡板图片
rightBlock = pygame.image.load(dirname + '/img/block.jpg');
rightBlockRect = rightBlock.get_rect();
rightBlockRect.centerx = 760;
rightBlockRect.centery = 300;


#定义画中线函数
def drawLine():
    lineColor = (255, 255, 255);
    for i in range(0, 40):
        start = (400, i * 15);
        end = (400, i * 15 + 10);
        pygame.draw.line(scene, lineColor, start, end, 4);


# 得分
leftScoreNum = 0;
rightScoreNum = 0;

# 左侧分数
def leftScoreShow():
    font = pygame.font.Font(None, 100); # 创建字体对象
    leftScore = font.render(str(leftScoreNum), 1, (255, 255, 255)); # 文本与颜色
    leftScoreRect = leftScore.get_rect();
    leftScoreRect.centerx = 200;
    leftScoreRect.centery = 70;
    scene.blit(leftScore, leftScoreRect); # 将左侧得分画到场景中上

# 右侧分数
def rightScoreShow():
    font = pygame.font.Font(None, 100); # 创建字体对象
    rightScore = font.render(str(rightScoreNum), 1, (255, 255, 255)); # 文本与颜色
    rightScoreRect = rightScore.get_rect();
    rightScoreRect.centerx = 600;
    rightScoreRect.centery = 70;
    scene.blit(rightScore, rightScoreRect); # 将右侧得分画到场景中上


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
                #回弹角度增益
                ballSpeedAngle = (ballRect.centery - leftBlockRect.centery)/50;

            isLeftBlockCrash = True;

    else :
        isLeftBlockCrash = False;


    if (ballRect.centerx < rightBlockRect.centerx + rightBlockRect.width / 2 and ballRect.centerx > rightBlockRect.centerx - rightBlockRect.width / 2) and (ballRect.centery < rightBlockRect.centery + rightBlockRect.height / 2 and ballRect.centery > rightBlockRect.centery - rightBlockRect.height / 2) :
        if isRightBlockCrash == False :
            if speedX > 0 :
                ballSpeedAngle = -(ballSpeedAngle - math.pi);

            else :
                #回弹角度增益
                ballSpeedAngle = (ballRect.centery - rightBlockRect.centery)/50;

            isRightBlockCrash = True;

    else :
        isRightBlockCrash = False;


# 获得pygame的时钟
fpsClock = pygame.time.Clock();

#定义小球移动速度
ballSpeed = 15;
#定义小球移动方向
ballSpeedAngle = 1/4 * math.pi;

#定义横杆移动速度
leftMoveSpeed = 0;
rightMoveSpeed = 0;




# 死循环确保窗口一直显示
while True:

    # 计算小球移动速度
    speedX = math.cos(ballSpeedAngle) * ballSpeed;
    speedY = math.sin(ballSpeedAngle) * ballSpeed;

    # 小球移动
    ballRect.centerx += speedX;
    ballRect.centery += speedY;

    # 左横杆移动
    leftBlockRect.centery += leftMoveSpeed;
    if(leftBlockRect.centery < 50):
        leftBlockRect.centery = 50;

    if(leftBlockRect.centery > 550):
        leftBlockRect.centery = 550;

    # 右横杆移动
    rightBlockRect.centery += rightMoveSpeed;
    if(rightBlockRect.centery < 50):
       rightBlockRect.centery = 50;

    if(rightBlockRect.centery > 550):
        rightBlockRect.centery = 550;


    # 碰撞上下边界
    if(ballRect.centery > 600):
        ballSpeedAngle = -ballSpeedAngle;

    if(ballRect.centery < 0):
        ballSpeedAngle = -ballSpeedAngle;

    if(ballRect.centerx > 800):
        ballSpeedAngle = -(ballSpeedAngle - math.pi);
        addScore(1); # 左边得分
        resetBall(1); # 重置小球并先向右发射

    if(ballRect.centerx < 0):
        ballSpeedAngle = -(ballSpeedAngle - math.pi);
        addScore(0);  # 右边得分
        resetBall(0); # 重置小球并先向左发射


    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
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



    scene.fill(bgColor);  # 填充黑色背景
    scene.blit(ball, ballRect);  # 将小球图片画到场景中上
    scene.blit(leftBlock, leftBlockRect);  # 将左侧挡板图片画到场景中上
    scene.blit(rightBlock, rightBlockRect);  # 将右侧挡板图片画到场景中上
    drawLine(); # 画中心虚线
    leftScoreShow(); # 左侧分数显示
    rightScoreShow(); # 右侧分数显示

    blockCrash(speedX); # 碰撞检测
    pygame.display.update();  # 更新全部显示

    fpsClock.tick(30);  # 设置pygame时钟的间隔时间
