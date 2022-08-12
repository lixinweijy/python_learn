import turtle as t
t.hideturtle()
t.speed(0)
t.screensize(900,900)
t.setup(900,900)
ss=[["black",0,350],["orange",0,80],["blue",0,-50],["brown",0,-250],
    ["green",-100,-250],["yellow",100,-250],["white",0,-350]]

hole=[[-250,-450],[-250,-30],[-250,390],[250,390],[250,-30],[250,-450]]

def ball_1(x,y):
    t.color("red")
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

def desk():
    t.penup()
    t.goto(-250,-420)
    t.color("black","mediumspringgreen")
    t.pendown()
    t.begin_fill()
    t.forward(500)
    t.left(90)
    t.forward(840)
    t.left(90)
    t.forward(500)
    t.left(90)
    t.forward(840)
    t.end_fill()
    t.penup()
    t.goto(-250,-230)
    t.color("green")
    t.pendown()
    t.setheading(0)
    t.forward(500)
    t.penup()
    t.goto(-100,-230)
    t.setheading(270)
    t.pendown()
    t.circle(100,180)
    t.setheading(0)
    
def hole1(x,y):
    t.color("black","gray")
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.circle(30,360)
    t.end_fill()


desk()
for j in range(5):    
    for i in range(1,j+2):
        ball_1(i,j)
for i in range(len(ss)):
    ball_2(ss[i][0],ss[i][1],ss[i][2])
for i in range(len(hole)):
    hole1(hole[i][0],hole[i][1])


t.done()