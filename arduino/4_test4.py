# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import serial
import turtle as t
ser = serial.Serial('COM3', 9600, timeout=1)
t1=t.Pen()
t1.hideturtle()
t2=t.Pen()
t2.hideturtle()
t.hideturtle()
s=[[-275,175],[-125,175],[25,175],[175,175],
   [-275,25],[-125,25],[25,25],[175,25],
   [-275,-125],[-125,-125],[25,-125],[175,-125],
   [-275,-275],[-125,-275],[25,-275],[175,-275]]
ss=[
    '1','2','3','+',
    '4','5','6','-',
    '7','8','9','*',
    'C','0','=','/'
]
def block(z,y,k,a):
    t.tracer(0)
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
    t.update()

t.tracer(0)
m=-150
flag=0
flag_2=0
for i in range(16):
    block(s[i][0], s[i][1], ss[i], "white")
t.update()
c=0
b=''
while 1:
    a=ser.readline().decode("utf-8")
    a=str.strip(a)
    if a!='':
        for i in range(16):
            if a==ss[i]:
                c=i
                block(s[i][0],s[i][1],ss[i],"skyblue")
                if i==12:
                    t.tracer(0)
                    t1.color("white","white")
                    t1.penup()
                    t1.goto(-150 + flag * 20, 325)
                    t1.pendown()
                    t1.begin_fill()
                    t1.setheading(0)
                    t1.forward(40)
                    t1.left(90)
                    t1.forward(40)
                    t1.left(90)
                    t1.forward(40)
                    t1.left(90)
                    t1.forward(40)
                    t1.end_fill()
                    t.update()
                    flag-=1
                    b=b[0:len(b)-1]
                    t1.color("black")
                    break
                if i==14:
                    flag_2=1
                    break
                flag += 1
                t1.penup()
                t1.goto(-150+flag*20,325)
                t1.pendown()
                t1.write(a,font=("",30,'normal'))
                b+=a
    else:
        block(s[c][0], s[c][1], ss[c], "white")
    if flag_2:
        t2.penup()
        t2.goto(0, 300)
        t2.pendown()
        b=eval(b)
        t2.write(b, font=("", 30, 'normal'))
        ser.write(b)
        b=''
        flag_2=0


