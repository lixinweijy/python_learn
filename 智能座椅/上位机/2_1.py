# -*- coding:utf-8 -*-

import serial
import turtle as t
t1=t.Pen()
t1.hideturtle()
t2=t.Pen()
t.tracer(0)
t1.penup()
t1.goto(-50,-100)
t1.pendown()
t1.forward(100)
t1.left(90)
t1.forward(200)
t1.penup()
t1.goto(-50,-100)
t1.pendown()
t1.forward(200)
t2.penup()
t2.goto(-70,110)
t2.pendown()
t.update()
t.hideturtle()
t2.hideturtle()

def block(x):
    if x<200:
        t.clear()
        t2.clear()
        t2.write(str(x)+"kg",font=("黑体",20,"normal"))
        t.tracer(0)
        t.penup()
        t.goto(-50,-100)
        t.pendown()
        t.setheading(0)
        t.begin_fill()
        t.forward(100)
        t.left(90)
        t.forward(x*2)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(x*2)
        t.end_fill()
        t.update()
ser = serial.Serial('COM3', 9600, timeout=1)
while 1:
    b=ser.readline().decode("utf-8")
    print(b)
    try:
        block(int(str(b)[:-7]))
    except:
        continue