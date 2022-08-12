import turtle as t
t.setup(600,600)
t.screensize(600,600)
t1=t.Pen()
t2=t.Pen()
t3=t.Pen()
t1.speed(0)
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t1.penup()
t1.goto(-245,-15)
t1.pendown()
t2.penup()
t2.goto(-30,30)
t2.pendown()
t3.penup()
t3.goto(15,30)
t3.pendown()
def half_circle():
    t1.setheading(180)
    t1.circle(-15,180)
    t1.forward(490)
    t1.circle(-15,180)
    t1.forward(490)
    t1.begin_fill()
    t1.circle(-15,180)
    t1.right(90)
    t1.forward(30)
    t1.left(90)
    t1.end_fill()

a=0
def block():
    t1.begin_fill()
    t1.forward(5)
    t1.left(90)
    t1.pencolor("white")
    t1.forward(30)
    t1.pencolor("black")
    t1.left(90)
    t1.forward(5)
    t1.left(90)
    t1.forward(30)
    t1.end_fill()
    t1.setheading(0)

half_circle()
block()
while(a<=100):
    if a==0:
        a=1
    t2.clear()
    t2.write(a,font=("华文彩云",20,"normal"))
    t3.write("%",font=("华文彩云",20,"normal"))
    if a<100:
        block()
        t1.penup()
        t1.forward(5)
        t1.pendown()
    else:
        t1.begin_fill()
        t1.circle(15,180)
        t1.left(90)
        t1.forward(30)
        t1.left(90)
        t1.end_fill()
    a+=1
    
