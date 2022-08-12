import datetime as dt
import turtle as t
nums=[[0,1,1,1,1,1,1],[0,1,0,0,0,0,1],[1,0,1,1,0,1,1],[1,1,1,0,0,1,1],
      [1,1,0,0,1,0,1],[1,1,1,0,1,1,0],[1,1,1,1,1,1,0],[0,1,0,0,0,1,1],
      [1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,0,0,0,0,0,0]]
t.pensize(10)
t.penup()
t.goto(-300,0)
t.speed(0)
def num(a):
    for i in range(7):
        t.pendown() if a[i] else t.penup()
        if i==3:
            t.forward(40)
        else:
            t.forward(40)
            t.right(90)
    t.setheading(0)
tm=str(dt.datetime.today())[0:10]
for i in (tm):
    try:
        i=int(i)
        num(nums[i])
        t.penup()
        t.forward(20)
        t.pendown()
    except:
        num(nums[10])
        t.penup()
        t.forward(20)
        t.pendown()
