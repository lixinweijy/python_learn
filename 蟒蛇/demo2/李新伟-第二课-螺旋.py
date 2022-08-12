import turtle as t
t.pensize(1)
t.speed(0)
a=10
for i in range(50):
    t.color('yellow')
    t.forward(a)
    t.right(90)
    a=a+2
    t.color('red')
    t.forward(a)
    t.right(90)
    a=a+2
    t.color('blue')
    t.forward(a)
    t.right(90)
    a=a+2
    t.color('green')
    t.forward(a)
    t.right(90)
    a=a+2
t.done()