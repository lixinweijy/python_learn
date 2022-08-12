#coding=gbk
import turtle as t

# 设置画笔速度和画布大小
t.speed(0)
t.setup(900,600)

# 定义红旗大小和颜色
def cloth():
    t.penup()
    t.goto(-450,-300)
    t.pendown()
    t.color('white', 'red')
    t.begin_fill()
    t.forward(900)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(900)
    t.left(90)
    t.forward(600)
    t.end_fill()

# 定义大红星
def star1():
    t.setheading(0)
    t.penup()
    t.goto(-400,200)
    t.pendown()
    t.color('', 'yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(150)
        t.right(144)
    t.end_fill()

# 定义小红星
def star2(x):
    t.setheading(x)
    t.penup()
    t.goto(-250,170)
    t.forward(150)
    t.pendown()
    t.color('', 'yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(50)
        t.right(144)
    t.end_fill()

# 把画布和大小星星合起来变成五星红旗
def flag():
    cloth()
    star1()
    star2(40)
    star2(14)
    star2(347)
    star2(320)

# 调用函数
flag()
# 隐藏画笔
t.hideturtle()