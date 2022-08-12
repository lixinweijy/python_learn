import turtle as t
t.pensize(1)
t.speed(0)
a=10
for i in range(25):
    t.color('yellow')
    t.penup()
    t.goto(a,a)
    t.pendown()
    t.goto(a,-a)
    t.goto(-a,-a)
    t.goto(-a,a)
    t.goto(a,a)
    a+=3

    t.color('red')
    t.penup()
    t.goto(a,a)
    t.pendown()
    t.goto(a,-a)
    t.goto(-a,-a)
    t.goto(-a,a)
    t.goto(a,a)
    a+=3

    t.color('blue')
    t.penup()
    t.goto(a,a)
    t.pendown()
    t.goto(a,-a)
    t.goto(-a,-a)
    t.goto(-a,a)
    t.goto(a,a)
    a+=3

    t.color('green')
    t.penup()
    t.goto(a,a)
    t.pendown()
    t.goto(a,-a)
    t.goto(-a,-a)
    t.goto(-a,a)
    t.goto(a,a)
    a+=3
