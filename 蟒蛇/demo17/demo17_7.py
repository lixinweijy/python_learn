import turtle as t
t.penup()
t.goto(-200,100)
t.pendown()
t.pencolor("red")
t.hideturtle()
t.setup(900,900)
t.screensize(900,900)
n=5
t.speed(0)
def koch(size,n):
    if n==0:
        t.forward(size)
    else:
        for i in (0,60,-120,60):
            t.left(i)
            koch(size/2,n-1)
for i in range(3):
    koch(100,n)
    t.right(120)
t.done()
