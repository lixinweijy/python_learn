import turtle as t
t.pensize(1)
t.speed(0)
a=10
for i in range(50):
    t.penup()
    t.goto(0,a)
    t.pendown()
    t.goto(a,0)
    t.goto(0,-a)
    t.goto(-a,0)
    t.goto(0,a)
    a+=3
t.done()