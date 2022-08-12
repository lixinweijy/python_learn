import turtle as t
t.pensize(2)
t.speed(0)
angle=45
a=5

for i in range(75):
    t.color('yellow')
    t.forward(a)
    t.right(angle)
    a+=1
    t.color('red')
    t.forward(a)
    t.right(angle)
    a+=1
    t.color('blue')
    t.forward(a)
    t.right(angle)
    a+=1
    t.color('green')
    t.forward(a)
    t.right(angle)
    a+=1
