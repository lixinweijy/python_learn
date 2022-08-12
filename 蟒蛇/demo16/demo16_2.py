import turtle as t
t.hideturtle()
t.color("red")
t.speed(0)

def ball(x,y):
    t.penup()
    t.goto(-y*20+x*40,-20-y*35)
    t.pendown()
    t.begin_fill()
    t.circle(20,360)
    t.end_fill()

for j in range(5):    
    for i in range(1,j+2):
        ball(i,j)

