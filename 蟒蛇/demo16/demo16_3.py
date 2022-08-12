import turtle as t
t.hideturtle()
t.color("red")
t.speed(0)
t.screensize(900,900)
ss=[["black",0,350],["orange",0,80],["blue",0,-50],["brown",0,-250],["green",-100,-250],["yellow",100,-250],["white",0,-350]]

def ball_1(x,y):
    t.penup()
    t.goto(-y*20+(x-1)*40,160+y*35)
    t.pendown()
    t.begin_fill()
    t.circle(20,360)
    t.end_fill()

def ball_2(x,y,z):
    t.color(x)
    t.penup()
    t.goto(y,z)
    t.pendown()
    t.begin_fill()
    t.circle(20,360)
    t.end_fill()

for j in range(5):    
    for i in range(1,j+2):
        ball_1(i,j)
for i in range(len(ss)):
    ball_2(ss[i][0],ss[i][1],ss[i][2])


