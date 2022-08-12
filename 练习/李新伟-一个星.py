#coding=gbk
import turtle as t

t.speed(0)
t.setup(900,600)


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

cloth()
star1()
t.hideturtle()