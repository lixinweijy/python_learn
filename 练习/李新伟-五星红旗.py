#coding=gbk
import turtle as t

# ���û����ٶȺͻ�����С
t.speed(0)
t.setup(900,600)

# ��������С����ɫ
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

# ��������
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

# ����С����
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

# �ѻ����ʹ�С���Ǻ�����������Ǻ���
def flag():
    cloth()
    star1()
    star2(40)
    star2(14)
    star2(347)
    star2(320)

# ���ú���
flag()
# ���ػ���
t.hideturtle()