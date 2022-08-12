import turtle as t
t.setup(800,600,200,200)
t.penup()
t.goto(0,-200)
t.speed(0)
t.pendown()
t.pencolor('red')
t.write('大家好，我是美女！',align='center',font=('华文琥珀',20,"normal"))
t.hideturtle()
def emogi(x,y):
    #脸
    t.pensize(3)
    t.speed(0)
    t.penup()
    t.goto(x,y)
    t.fillcolor('yellow')
    t.begin_fill()
    t.pendown()
    t.pencolor('orange')
    t.circle(150)
    t.end_fill()

    #嘴
    t.pencolor('brown')
    t.setheading(90)
    t.penup()
    t.forward(50)
    t.setheading(0)
    t.pendown()
    t.circle(100,60)
    t.circle(100,-120)
    t.circle(100,60)

    #右眼
    t.penup()
    t.setheading(90)
    t.forward(150)
    t.setheading(0)
    t.forward(50)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.pencolor('black')
    t.fillcolor('black')
    t.begin_fill()
    t.circle(13)
    t.end_fill()

    #左眼
    t.pencolor('brown')
    t.penup()
    t.setheading(180)
    t.forward(100)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.setheading(0)
    t.circle(20,360)
    t.end_fill()
    t.pencolor('black')
    t.fillcolor('black')
    t.begin_fill()
    t.circle(13)
    t.end_fill()
    t.hideturtle()

def hair(x,y):
    for i in range(7):
        t.pensize(20)
        if i==0:
            color="red"
        elif i==1:
            color="orange"
        elif i==2:
            color="yellow"
        elif i==3:
            color="green"
        elif i==4:
            color="cyan"
        elif i==5:
            color="blue"
        elif i==6:
            color="purple"
        t.penup()
        t.setheading(x)
        t.pencolor(color)
        t.goto(0,100-20*i)
        t.pendown()
        t.circle(y,80)

hair(110,300)
hair(70,-300)

t.penup()
t.goto(0,0)
t.setheading(0)
t.pendown()
emogi(0,-150)

t.done()