from turtle import *

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

