# -*- coding:utf-8 -*-
import serial
import turtle as t
ser = serial.Serial('COM3', 9600, timeout=1)
t1=t.Pen()
t1.hideturtle()
t.hideturtle()
s=[[-275,175],[-125,175],[25,175],[175,175],
   [-275,25],[-125,25],[25,25],[175,25],
   [-275,-125],[-125,-125],[25,-125],[175,-125],
   [-275,-275],[-125,-275],[25,-275],[175,-275]]
ss=[
    '1','2','3','+',
    '4','5','6','-',
    '7','8','9','x',
    '*','0','=','/'
]
def block(z,y,k,a):
    t.color('black',a)
    t.penup()
    t.goto(z,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.end_fill()
    t.penup()
    t.goto(z + 30, y + 10)
    t.pendown()
    t.write(k, font=("", 60, "normal"))
t.tracer(0)
for i in range(16):
    block(s[i][0], s[i][1], ss[i], "white")
t.update()
c=0
while 1:
    a=ser.readline().decode("utf-8")
    a=str.strip(a)
    if a!='':
        for i in range(16):
            if a==ss[i]:
                block(s[i][0],s[i][1],ss[i],"skyblue")
                c=i
    else:
        block(s[c][0], s[c][1], ss[c], "white")


