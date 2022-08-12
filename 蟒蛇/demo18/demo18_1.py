import turtle as t
one=[0,1,0,0,0,0,1]
t.pensize(10)
def num(a):
    for i in range(len(one)):
        t.pendown() if one[i] else t.penup()
        if i==3:
            t.forward(40)
        else:
            t.forward(40)
            t.right(90)
    t.left(90)
num(one)
    
