# -*- coding:utf-8 -*-
import datetime as dt
import turtle as t
nums={"0":[0,1,1,1,1,1,1],"1":[0,1,0,0,0,0,1],"2":[1,0,1,1,0,1,1],"3":[1,1,1,0,0,1,1],
      "4":[1,1,0,0,1,0,1],"5":[1,1,1,0,1,1,0],"6":[1,1,1,1,1,1,0],"7":[0,1,0,0,0,1,1],
      "8":[1,1,1,1,1,1,1],"9":[1,1,1,0,1,1,1],"-":[1,0,0,0,0,0,0]}
week=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
t2=t.Pen()
t1=t.Pen()
t1.hideturtle()
t1.pensize(10)
t.hideturtle()
t.pensize(10)
def num(a,b):
    if b:
        t=t1
    else:
        t=t2
    for i in range(7):
        t.penup()
        t.forward(7)
        t.pendown() if a[i] else t.penup()
        t.forward(40)
        t.penup()
        t.forward(7)
        if i!=3:
            t.right(90)
    t.setheading(0)
    t.penup()
    t.forward(20)
    t.pendown()
def maohao():
    t.penup()
    t.forward(50)
    t.left(90)
    t.forward(15)
    t.pendown()
    t.forward(5)
    t.left(180)
    t.penup()
    t.forward(35)
    t.pendown()
    t.forward(5)
    t.penup()
    t.backward(20)
    t.setheading(0)
    t.forward(20)
    t.pendown()

while(1):
    t.tracer(0)
    t1.penup()
    t1.goto(-300, 200)
    t1.pendown()
    tm = str(dt.datetime.today())[0:10]
    for i in (tm):
        num(nums[i], 1)
    # 打印周
    wk = dt.datetime.today().weekday()
    t.penup()
    t.goto(-70, 0)
    t.pendown()
    t.write(week[wk], font=("华文琥珀", 50, "normal"))
    time = str(dt.datetime.today())[11:19]
    t.clear()
    t.penup()
    t.goto(-250, -150)
    t.pendown()
    for i in (time):
        if i != ":":
            num(nums[i], 0)
        else:
            maohao()
    t.update()