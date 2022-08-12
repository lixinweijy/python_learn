import turtle as t

t.pensize(5)
t.speed(0)
t.up()
t.goto(0,-200)
t.pendown()
t.color('black','pink')
t.begin_fill()
t.left(50)
t.forward(300)

for i in range(220):
    t.forward(2)
    t.left(1)

t.right(180)
for i in range(220):
    t.forward(2)
    t.left(1)


t.left(2)
t.forward(310)
t.hideturtle()
t.end_fill()
