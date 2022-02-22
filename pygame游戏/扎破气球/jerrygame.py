from turtle import *
from random import randrange,choice
import pygame
import time
"""定义变量"""
balloons = []
color_option = ['red','black','yellow','pink','green','purple','light blue','orange','gray']
size = 50
"""定义函数"""

def puton_music1():
    file1 = r'.//dist//气球爆炸.wav'# 音乐路径
    pygame.mixer.init()  # 初始化
    track = pygame.mixer.Sound(file1)  # 加载音乐文件
    track.play()  # 开始播放音乐

def line(x,y,c,d,line_width=1,color_name='black'):
    up()
    goto(x,y)
    down()
    color(color_name)
    width(line_width)
    goto(c,d)
def distance(x,y,a,b):
    return ((x-a)**2+(y-b)**2)**0.5
def tap(x,y):
    for i in range(len(balloons)):
        if distance(x,y,balloons[i][0],balloons[i][1]) < size/2:
            puton_music1()
            balloons.pop(i)
def draw():
    clear() #清除画布
    for i in range(1,len(balloons)+1):
        line(balloons[-i][0],balloons[-i][1],balloons[-i][0],balloons[-i][1]-1.5*size)
        up()
        goto(balloons[-i][0],balloons[-i][1])
        dot(size,balloons[-i][2])
        balloons[-i][1] = balloons[-i][1] + 1.5
    update()    #修改画布
pygame.mixer.init()
file = r'.//dist//经典游戏背景音乐.wav'
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
def gameLoop():
    if randrange(0,40) == 1 :
        x = randrange(-200+size,200-size)
        c = choice(color_option)
        balloons.append([x,-200-size,c])
    draw()
    ontimer(gameLoop,20)

setup(width=420,height=420,startx=0,starty=0)
hideturtle()
tracer(False)
listen()
onscreenclick(tap)
gameLoop()
done()  #结束函数，画布停留

