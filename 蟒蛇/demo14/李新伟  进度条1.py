import turtle as t
t.setup(900,900)
t.screensize(900,900)

t1=t.Pen()
t2=t.Pen()
t3=t.Pen()
t1.speed(0)
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t1.penup()
t1.goto(-380,-15)
t1.pendown()
t2.penup()
t2.goto(-20,30)
t2.pendown()
t3.penup()
t3.goto(25,30)
t3.pendown()
t1.color("white","black")

a=0
def block():
    t1.begin_fill()
    t1.forward(20)
    t1.left(90)
    t1.forward(30)
    t1.left(90)
    t1.forward(20)
    t1.left(90)
    t1.forward(30)
    t1.end_fill()
    t1.setheading(0)

while(a<=100):
    block()
    t1.penup()
    t1.forward(30)
    t1.pendown()
    t2.clear()
    t2.write(a,font=("华文彩云",20,"normal"))
    t3.write("%",font=("华文彩云",20,"normal"))
    a+=4