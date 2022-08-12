import turtle as t
t.speed(2)
t.penup()
t.goto(0,-200)
t.pendown()
t.left(90)
t.color("green")
def tree(n,x):
    if n>0:
        t.forward(x)
        t.left(30)
        tree(n-1,x*0.8)
        t.right(60)
        tree(n-1,x*0.8)
        t.left(30)
        t.backward(x)

        
tree(5,100)
t.done()
