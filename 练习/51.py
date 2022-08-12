# -*- coding:utf-8 -*-
import turtle as t
import datetime as dt

t.setup(1100, 600)
t1 = t.Pen()
t2 = t.Pen()
t1.hideturtle()
t2.hideturtle()
tm = dt.datetime.today()
s = [[0, 1, 1, 1, 1, 1, 1, '0'], [0, 1, 0, 0, 0, 0, 1, '1'], [1, 0, 1, 1, 0, 1, 1, '2'], \
     [1, 1, 1, 0, 0, 1, 1, '3'], [1, 1, 0, 0, 1, 0, 1, '4'], [1, 1, 1, 0, 1, 1, 0, '5'], \
     [1, 1, 1, 1, 1, 1, 0, '6'], [0, 1, 0, 0, 0, 1, 1, '7'], [1, 1, 1, 1, 1, 1, 1, '8'], \
     [1, 1, 1, 0, 1, 1, 1, '9'], [1, 0, 0, 0, 0, 0, 0, '-'], [0, 1, 0, 0, 0, 0, 1, '`']]
ss = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
sss = [t1, t2]
t1.pensize(7)
t2.pensize(7)
t1.penup()
t1.goto(-400, 0)
t1.pendown()


def hhh(bh, b):
    b.penup()
    b.fd(5)
    b.pendown() if bh == 1 else b.penup()
    b.fd(20)
    b.penup()
    b.fd(5)
    b.pendown()


def dian(b):
    b.penup()
    b.right(90)
    b.fd(5)
    b.pendown()
    b.fd(3)
    b.penup()
    b.backward(13)
    b.pendown()
    b.backward(3)
    b.penup()
    b.fd(8)
    b.left(90)
    b.fd(30)
    b.pendown()


def hui(a, b):
    if a != '-' and a != ':':
        b.setheading(0)
        a = int(a)
        for i in range(3):
            hhh(s[a][i], b)
            b.right(90)
        for i in range(3, 5):
            hhh(s[a][i], b)
        b.right(90)
        for i in range(5, 6):
            hhh(s[a][i], b)
            b.right(90)
        hhh(s[a][6], b)
        b.setheading(0)
        b.penup()
        b.fd(40)
        b.pendown()
    elif a == '-':
        hui(10, b)
    else:
        dian(b)


t.tracer(0)
for i in range(1, len(str(tm)[0:-15])):
    hui(str(tm)[i - 1:i], sss[0])

a = tm.weekday()
t1.penup()
t1.goto(-60, -100)
t1.pendown()
t1.write(ss[a], font=('华文行楷', 30,"normal"))

t2.penup()
t2.goto(-200, -150)
t2.pendown()
t.tracer(1)

while (1):
    t.tracer(0)
    tm = dt.datetime.today()
    t2.clear()
    for i in range(12, 20):
        hui(str(tm)[i - 1:i], sss[1])
    t.tracer(1)
    t2.penup()
    t2.goto(-200, -150)
    t2.pendown()
