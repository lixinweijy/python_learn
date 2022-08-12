# coding=gbk
import turtle as t
t.speed(1)
t.setup(600,900)

#2  x,y为位置，z为1正，否则反
#4  x,y为位置，z为1正，否则反
def fan(a,b,c,d,e):
    t.penup()
    t.goto(a,b)
    t.pendown()
    if d==1:
        d="black"
    else:
        d="red"
    t.fillcolor(d)
    t.begin_fill()
    if e==1:
        t.setheading(300)
        t.forward(c*6/5)
        t.right(60)
        t.forward(c*6/5)
        t.right(120)
        t.forward(c*6/5)
        t.right(60)
        t.forward(c*6/5)
    else:
        t.setheading(60)
        t.forward(c * 6 / 5)
        t.left(60)
        t.forward(c * 6 / 5)
        t.left(120)
        t.forward(c * 6 / 5)
        t.left(60)
        t.forward(c * 6 / 5)
    t.end_fill()

fan(0,0,50,-1,-1)
t.hideturtle()
t.done()