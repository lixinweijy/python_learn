#coding=gbk
import turtle as t
import random as r
t.setup(900,900)
t.screensize(900,900)
#设置四支画笔
t1=t.Pen()
t2=t.Pen()
t3=t.Pen()
t4=t.Pen()
#初始化画笔的颜色，速度，位置
def initial():
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t4.hideturtle()
    t1.speed(0)
    t2.speed(0)
    t1.color("green","green")
    t2.color("green","green")
    t3.penup()
    t3.goto(25,200)
    t3.pendown()
    t4.penup()
    t4.goto(-20,200)
    t4.pendown()
#画出电池形状外观
def frame():
    t1.penup()
    t1.goto(100,0)
    t1.pendown()
    t1.left(90)
    t1.forward(396)
    t1.left(90)
    t1.forward(95)
    t1.right(90)
    t1.forward(15)
    t1.left(90)
    t1.forward(10)
    t1.left(90)
    t1.forward(15)
    t1.right(90)
    t1.forward(95)
    t1.left(90)
    t1.forward(396)
    t1.left(90)
    t1.forward(200)
    t1.left(90)
#画出增加的电量
def block(a):
    if a<100:
        t1.begin_fill()
        t1.forward(4)
        t1.left(90)
        t1.pencolor("white")
        if a == 99:
            t1.pencolor("green")
        t1.forward(200)
        t1.pencolor("green")
        t1.left(90)
        t1.forward(4)
        t1.left(90)
        t1.forward(200)
        t1.end_fill()
        t1.left(90)
        t1.forward(4)
    else: #最后百分之百的情况要变一种画法
        t1.begin_fill()
        t1.left(90)
        t1.forward(95)
        t1.right(90)
        t1.forward(15)
        t1.left(90)
        t1.forward(10)
        t1.left(90)
        t1.forward(15)
        t1.left(90)
        t1.forward(10)
        t1.end_fill()
#画出圆圈
def t2_pen(q):
    #圆圈的横坐标是在-100到100内变化的
    x=r.randint(-100,100)
    t2.penup()
    t2.clear() #每画出一个圆圈清除上一个圆圈
    t2.goto(x,q*20-300)  #圆圈不断上升
    t2.begin_fill()
    t2.circle(q,360)
    t2.end_fill()
a=0  #用来记录电池电量
q=5  #用来实现圆圈上升
#准备工作
initial()
frame()
while(a<100):
    a+=1
    q+=1
    if q==15:
        q=5
    t2_pen(q)  #画圆圈
    t4.clear()
    t4.write(a, font=("华文琥珀", 20, "normal"))  #画电量
    t3.write("%", font=("华文彩云", 20, "normal")) #画百分号
    block(a)  #增加电量