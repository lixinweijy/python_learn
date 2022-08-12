# -*- coding:utf-8 -*-
import serial
import turtle as t
ser = serial.Serial('COM3', 9600, timeout=1)
t.hideturtle()
t.penup()
t.goto(-300,-300)
t.pendown()
t.tracer(0)
t.forward(600)
t.left(90)
t.forward(600)
t.left(90)
t.forward(600)
t.left(90)
t.forward(600)
t.left(90)
t.forward(150)
t.left(90)
t.forward(600)
t.right(90)
t.forward(150)
t.right(90)
t.forward(600)
t.left(90)
t.forward(150)
t.left(90)
t.forward(600)
t.right(90)
t.forward(150)
t.right(90)
t.forward(150)
t.right(90)
t.forward(600)
t.left(90)
t.forward(150)
t.left(90)
t.forward(600)
t.right(90)
t.forward(150)
t.right(90)
t.forward(600)
t.left(90)
t.forward(150)
t.update()
t.fillcolor("black")
def num(w,y,z):
    t.penup()
    t.goto(w+40,y+10)
    t.pendown()
    t.write(z,font=("",100,"normal"))
num(-300,-300,"*")
num(-150,-300,"0")
num(0,-300,"#")
num(150,-300,"%")
num(-300,-150,"7")
num(-150,-150,"8")
num(0,-150,"9")
num(150,-150,"x")
num(-300,0,"4")
num(-150,0,"5")
num(0,0,"6")
num(150,0,"-")
num(-300,150,"1")
num(-150,150,"2")
num(0,150,"3")
num(150,150,"+")

def block(z,y):
    t.penup()
    t.goto(z,y)
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(150)
    t.end_fill()
while 1:
    a=ser.readline().decode("utf-8")
    print(a)
    if a==1:
        block(-300,150)
    elif a==2:
        block(-150, 150)
    elif a==3:
        block(0, 150)
    elif a==4:
        block(-300, 0)
    elif a==5:
        block(-150, 0)
    elif a==6:
        block(0, 0)
    elif a==7:
        block(-300, -150)
    elif a==8:
        block(-150, -150)
    elif a==9:
        block(0, -150)
    elif a=="A":
        block(150, 150)
    elif a=="B":
        block(150, 0)
    elif a=="C":
        block(150, -150)
    elif a=="D":
        print(3)
        block(150, -300)
    elif a=="0":
        block(-150, -300)
    elif a=="#":
        block(0, -300)
    elif a=="*":
        block(-300, -300)
