import turtle as t
t.speed(0)
t.setup(600,900)

#写A
def A(x,y):
    t.penup()
    t.goto(x,y)
    t.pensize(4)
    t.pencolor('red')
    t.write("A",align='center',font=("楷体",50))

def xin(a,b,c,d,e):
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    t.setheading(e)
    t.forward(c)
    t.setheading(d)
    if e>180:
        t.circle(-c/4,180)
        t.setheading(d)
        t.circle(-c/4,180)
    else:
        t.circle(c/4,180)
        t.setheading(d)
        t.circle(c/4,180)
    t.setheading(360-e)
    t.forward(c)
    t.end_fill()
    
#a为横坐标，b为纵坐标，c为大小,d,e为方向

A(-250,350)
xin(-250,250,70,90,60)
xin(0,90,150,-90,300)
t.done()
t.hideturtle()

