#coding=gbk
import turtle as t
import random as r
#初始化画笔
t.setup(800, 800)
t.screensize(800, 800)
t1 = t.Pen()
t2 = t.Pen()
t3 = t.Pen()
t4=t.Pen()
t1.speed(0)
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
def two_circle():  # 画圆环
    t1.penup()
    t1.goto(0, -300)
    t1.pendown()
    t1.circle(300, 360)
    t1.penup()
    t1.goto(0, -250)
    t1.pendown()
    t1.circle(250, 360)
def initial_space():  # 初始化位置
    t2.penup()
    t2.goto(-20, 20)
    t2.pendown()
    t3.penup()
    t3.goto(25, 20)
    t3.pendown()
    t4.penup()
    t4.goto(0,-20)
    t4.pendown()
    t1.penup()
    t1.goto(0, 275)
    t1.pendown()
def clr():  #调颜色
    q="#"
    for i in range(6):
        i=r.randint(48,70)
        if 57<i<65:
            i=i-7
        q+=chr(i)
    return q
def t4_color_change():
    global b
    if b==1:
        t4.clear()
        t4.write("LANDING",align="center", font=("华文彩云", 25, "normal"))
    elif b==2:
        t4.clear()
        t4.write("LANDING.", align="center", font=("华文彩云", 25, "normal"))
    elif b==3:
        t4.clear()
        t4.write("LANDING..", align="center", font=("华文彩云", 25, "normal"))
    else:
        t4.clear()
        t4.write("LANDING...", align="center", font=("华文彩云", 25, "normal"))
        b=0
two_circle()
t1.pensize(50)
t1.pencolor("red")
initial_space()
a = 0
b=3
clr()
while (a <=100):
    t.bgcolor(clr())
    t1.color(clr())
    t2.clear()
    t4.color(clr())
    t2.write(a, font=("华文琥珀", 20, "normal"))
    t3.write("%", font=("华文琥珀", 20, "normal"))
    b+=1
    t4_color_change()
    t1.circle(-275, 3.6)
    a+=1
t.done()
