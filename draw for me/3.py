import turtle as t
t.pensize(5)
t.speed(0)
t.penup()
t.goto(0,100)
t.color('black','blue')
for i in range(360):
    t.color('black', 'blue')
    t.pendown()
    t.begin_fill()
    t.forward(2)
    t.left(1)
    t.end_fill()

for i in range(360):
    t.color('black', 'blue')
    t.pendown()
    t.begin_fill()
    t.forward(4)
    t.right(1)
    t.end_fill()
