import turtle as t
t.hideturtle()
t.color("red")
t.speed(0)
for i in range(5):
    t.penup()
    t.goto(-80+i*40,-20)
    t.pendown()
    t.begin_fill()
    t.circle(20,360)
    t.end_fill()
