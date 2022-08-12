import datetime as dt
import turtle as t
# 初始化数据
nums={"0":[0,1,1,1,1,1,1],"1":[0,1,0,0,0,0,1],"2":[1,0,1,1,0,1,1],"3":[1,1,1,0,0,1,1],
      "4":[1,1,0,0,1,0,1],"5":[1,1,1,0,1,1,0],"6":[1,1,1,1,1,1,0],"7":[0,1,0,0,0,1,1],
      "8":[1,1,1,1,1,1,1],"9":[1,1,1,0,1,1,1],"-":[1,0,0,0,0,0,0]}
week=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
#初始化画笔
t1=t.Pen()
t1.hideturtle()
t1.pensize(10)
t2=t.Pen()
t2.hideturtle()
t2.pensize(10)

# 画数字
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

#画冒号
def maohao():
    t2.penup()
    t2.forward(50)
    t2.left(90)
    t2.forward(15)
    t2.pendown()
    t2.forward(5)
    t2.left(180)
    t2.penup()
    t2.forward(35)
    t2.pendown()
    t2.forward(5)
    t2.penup()
    t2.backward(20)
    t2.setheading(0)
    t2.forward(20)
    t2.pendown()

# 打印日期
def day():
    t.tracer(0)
    # 打印年月日
    t1.penup()
    t1.goto(-320, 200)
    t1.pendown()
    tm = str(dt.datetime.today())[0:10]
    for i in (tm):
        num(nums[i],1)
    # 打印周
    wk = dt.datetime.today().weekday()
    t1.penup()
    t1.goto(-70, 0)
    t1.pendown()
    t1.write(week[wk], font=("华文琥珀", 50, "normal"))
    t.update()

# 打印时间
def tim():
    flag = 0
    time = str(dt.datetime.today())[11:19]
    t.tracer(0)
    t2.clear()
    t2.penup()
    t2.goto(-250, -150)
    t2.pendown()
    for i in (time):
        if i=="0":
            flag+=1
        if i != ":":
            num(nums[i],0)
        else:
            maohao()
    if flag==6:
        t1.clear()
        day()
    t.update()

day()
# 更新时间
while(1):
    tim()