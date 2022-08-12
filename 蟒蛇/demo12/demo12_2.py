import turtle as t
import random as r
t.setup(900,900)
t.hideturtle()
while True:
    bold=r.randint(3,10)
    color=r.randint(1,7)
    direct=r.randint(0,360)
    distance=r.randint(20,50)
    speed=r.randint(0,4)
    if speed==1:
        speed=10
    elif speed==2:
        speed=9
    elif speed==3:
        speed=8
    else:
        speed=7
    x=t.xcor()
    y=t.ycor()
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
    if x>350 or x<-350:
        t.left(180)
    if y>350 or y<-350:
        t.left(180)
    t.speed(speed)
    t.left(direct)
    t.pensize(bold)
    t.pencolor(color)
    t.forward(distance)

    bgclr=r.randint(1,7)
    sleep=r.randint(1,3)
    if bgclr==1:
        bgclr="white"
    elif bgclr==2:
        bgclr="brown"
    elif bgclr==3:
        bgclr="pink"
    elif bgclr==4:
        bgclr="coral"
    elif bgclr==5:
        bgclr="gray"
    elif bgclr==6:
        bgclr="khaki"
    else:
        bgclr="skyblue"
    while(sleep>0):
        t.bgcolor(bgclr)
        sleep-=1

