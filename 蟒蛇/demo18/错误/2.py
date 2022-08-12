# -*- coding:utf-8 -*-
import datetime as dt
import turtle as t
nums={"0":[0,1,1,1,1,1,1],"1":[0,1,0,0,0,0,1],"2":[1,0,1,1,0,1,1],"3":[1,1,1,0,0,1,1],
      "4":[1,1,0,0,1,0,1],"5":[1,1,1,0,1,1,0],"6":[1,1,1,1,1,1,0],"7":[0,1,0,0,0,1,1],
      "8":[1,1,1,1,1,1,1],"9":[1,1,1,0,1,1,1],"-":[1,0,0,0,0,0,0]}
week=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
t.hideturtle()
t.pensize(10)
def num(a):
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
def ll():
    t.clear()
    # 打印日期
    t.penup()
    t.goto(-300, 200)
    t.pendown()
    tm = str(dt.datetime.today())[0:10]
    for i in (tm):
        num(nums[i])
    # 打印周
    wk = dt.datetime.today().weekday()
    t.penup()
    t.goto(-70, 0)
    t.pendown()
    t.write(week[wk], font=("华文琥珀", 50, "normal"))
    # 打印时间
    time = str(dt.datetime.today())[11:19]
    t.penup()
    t.goto(-250, -150)
    t.pendown()
    for i in (time):
        if i != ":":
            num(nums[i])
        else:
            maohao()

while(1):
    t.tracer(0)
    ll()
    t.tracer(1)
    # print(1)
    t.penup()
    t.forward(100)
    t.pendown()
    # t.delay(100)
    # print(1)