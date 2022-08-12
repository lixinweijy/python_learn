import turtle as t
import random as r
t.hideturtle()
while True:
    bold=r.randint(3,10)
    color=r.randint(1,7)
    direct=r.randint(0,360)
    distance=r.randint(20,50)
    speed=r.randint(1,10)
    if color==1:
        color="red"
    elif color==2:
        color="orange"
    elif color==3:
        color="yellow"
    elif color==4:
        color="green"
    elif color==5:
        color="blue"
    elif color==6:
        color="black"
    else:
        color="purple"
    t.speed(speed)
    t.left(direct)
    t.pensize(bold)
    t.pencolor(color)
    t.forward(distance)
