# coding=gbk
import turtle as t
t.speed(1)
def mei(a,b,c,d,e):
    t.pensize(1)
    t.color("", "black")
    x=270
    if e!=1:
        x=360-x
        t.penup()
        t.goto(a + d * 7 / 8, b + d / 4)
        d = -d
        t.pendown()
    else:
        t.penup()
        t.goto(a + d / 8, b + d * 5 / 4)
        t.pendown()
    t.begin_fill()
    t.penup()
    t.setheading(x)
    t.forward(c/10)
    t.left(210)
    t.pendown()
    t.circle(c/20,360)
    t.end_fill()
    t.begin_fill()
    t.right(60)
    t.circle(-c/20,360)
    t.end_fill()
    t.begin_fill()
    t.left(120)
    t.circle(-c/20,360)
    t.end_fill()
    t.begin_fill()
    t.left(80)
    t.forward(c*2/15)
    t.left(100)
    t.forward(c/20)
    t.left(100)
    t.forward(c*2/15)
    t.end_fill()

mei(0,-200,300,300,1)
t.hideturtle()
t.done()