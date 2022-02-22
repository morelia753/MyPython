
import turtle
from turtle import *
from random import randrange
from time import sleep
import pygame

snake = [[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]
apple_x = randrange(-20,18)*10
apple_y = randrange(-19,19)*10
aim_x = 10
aim_y = 0


def square(x,y,size,color_name):

    up()
    goto(x,y)
    down()
    #设置颜色
    color(color_name)
    #填充
    begin_fill()

    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)

    end_fill()

def change(x,y):
    global aim_x,aim_y
    aim_x = x
    aim_y = y

def inside_snake():
    for i in range(len(snake)-1):
        if snake[i][0] == snake[-1][0] and snake[i][1] == snake[-1][1]:
        #蛇咬住自己
            return True
    return False

def inside_map():
    if -200 <= snake[-1][0] <= 180 and -190 <= snake[-1][1] <= 190:
        #没出界
        return True
    else:
        return False
def sound1():       #播放吃食物音效
    file1 =r'./dist/吃食物音效.mp3'
    #初始化混音器模块
    pygame.mixer.init()
    #创建声音对象
    track = pygame.mixer.Sound(file1)
    #播放
    track.play()
def sound2():       #播放蛇over音效
    file2 = r'./dist/贪吃蛇挂了.mp3'
    pygame.mixer.init()
    track = pygame.mixer.Sound(file2)
    track.play()

pygame.mixer.init()
file = r'./dist/贪吃蛇大作战背景音乐.mp3'
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

def gameLoop():
    global apple_x,apple_y,snake,aim_x,aim_y

    snake.append([snake[-1][0]+aim_x,snake[-1][1]+aim_y])

    if snake[-1][0] != apple_x or snake[-1][1] != apple_y:
        snake.pop(0)
    else:
        #迟到食物
        sound1()    #播放音效
        #更新食物位置
        apple_x = randrange(-20, 18)*10
        apple_y = randrange(-19, 19)*10

    #出界或者蛇咬住自己,结束
    if (not inside_map()) or inside_snake():
        square(snake[-1][0],snake[-1][1],10,"red")
        update()
        #播放游戏结束音效
        sound2()
        #等待两秒重开
        sleep(2)
        snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]
        apple_x = randrange(-20, 18)*10
        apple_y = randrange(-19, 19)*10
        aim_x = 10
        aim_y = 0

    clear()
    square(-210, -200, 410, "black")
    square(-200, -190, 390, "white")
    square(apple_x, apple_y, 10, "red")
    for i in range(len(snake)):
        square(snake[i][0],snake[i][1],10,"black")
    #更新
    update()
    #过130ms再次执行gameLoop
    ontimer(gameLoop,130)

#画布
turtle.setup(420, 420, 0, 0)
hideturtle()
#隐藏绘图，直接显示绘画效果
tracer(False)
#监视键盘和鼠标操作
listen()
#右手操控
onkey(lambda: change(0,10), "Up")
onkey(lambda: change(0,-10), 'Down')
onkey(lambda: change(10,0), 'Right')
onkey(lambda: change(-10,0), 'Left')
#左手操控
onkey(lambda: change(0,10), "w")
onkey(lambda: change(0,-10), 's')
onkey(lambda: change(10,0), 'd')
onkey(lambda: change(-10,0), 'a')
sleep(3)
gameLoop()

done()
