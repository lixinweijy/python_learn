import turtle as t
t.setup(800,800)
t.screensize(800,800)

t1=t.Pen()
t2=t.Pen()
t3=t.Pen()
t1.speed(0)
t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

def two_circle():#画圆环
    t1.penup()
    t1.goto(0,-300)
    t1.pendown()
    t1.circle(300,360)
    t1.penup()
    t1.goto(0,-250)
    t1.pendown()
    t1.circle(250,360)
a=0
b=0
c=0
d=0
def initial_space():#初始化位置
    t2.penup()
    t2.goto(-20,0)
    t2.pendown()
    t3.penup()
    t3.goto(25,0)
    t3.pendown()
    t1.penup()
    t1.goto(0,275)
    t1.pendown()

two_circle()
t1.pensize(50)
t1.pencolor("red")
initial_space()
while(d<360):
    t1.circle(-275,1)
    t3.write("%",font=("华文彩云",20,"normal"))
    b+=1
    d+=1
    if c>5:
        c-=5
    else:
        if c<=2:
            if b==3:
                a+=1
                b=0
                c+=1
                t2.clear()
                t2.write(a,font=("华文彩云",20,"normal"))
        else:
            if b==4:
                a+=1
                b=0
                c+=1
                t2.clear()
                t2.write(a,font=("华文彩云",20,"normal"))