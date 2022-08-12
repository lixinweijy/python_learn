import turtle as t
t.speed(0)
t.setup(600,900)

def two(x,y):
    t.penup()
    t.goto(x,y)
    t.pensize(5)
    t.pencolor('red')
    t.pendown()
    t.setheading(180)
    t.forward(33)
    t.setheading(60)
    t.forward(60)
    t.setheading(90)
    t.circle(18,180)

def two1(x,y):
    t.penup()
    t.goto(x,y)
    t.pensize(5)
    t.pencolor('red')
    t.pendown()
    t.setheading(0)
    t.forward(33)
    t.setheading(240)
    t.forward(60)
    t.setheading(270)
    t.circle(18,180)



def xin(a,b,c,e):
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    if e>180:
        t.setheading(e)
        t.forward(c)
        t.circle(-c*0.414,225)
        t.setheading(-90)
        t.circle(-c*0.414,225)
    else:
        t.setheading(e)
        t.forward(c)
        t.circle(c*0.414,225)
        t.setheading(90)
        t.circle(c*0.414,225)
    t.setheading(360-e)
    t.forward(c)
    t.end_fill()
#a为横坐标，b为纵坐标，c为大小,e为方向

two(-235,360)
xin(-250,280,50,45)
xin(0,400,80,315)
xin(0,-400,100,45)
xin(250,-280,50,315)
two1(235,-360)
t.hideturtle()
t.done()
