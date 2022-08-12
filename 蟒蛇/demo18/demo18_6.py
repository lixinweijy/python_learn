import datetime as dt
import turtle as t
# 数据
nums=[[0,1,1,1,1,1,1],[0,1,0,0,0,0,1],[1,0,1,1,0,1,1],[1,1,1,0,0,1,1],
      [1,1,0,0,1,0,1],[1,1,1,0,1,1,0],[1,1,1,1,1,1,0],[0,1,0,0,0,1,1],
      [1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,0,0,0,0,0,0]]
# 定义一个返回星期的函数
week=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
# 初始化画笔
t.tracer(0)
t.pensize(10)
t.penup()
t.goto(-300,200)
t.hideturtle()
t1=t.Pen()
t1.hideturtle()
t1.penup()
t1.goto(-210,-180)
t1.pendown()
# 定义一个画数字的函数
def num(a):
    for i in range(7):
        t.pendown() if a[i] else t.penup()
        t.forward(40)
        if i!=3:
            t.right(90)
    t.setheading(0)
# 获取年月日
tm=str(dt.datetime.today())[0:10]
# 打印年月日
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
# 获取星期
wk=dt.datetime.today().weekday()

# 打印星期
t.penup()
t.goto(-70,0)
t.pendown()
t.write(week[wk],font=("华文琥珀",50,"normal"))
t.update()
# 重复打印并更新时间
while(1):
    time=str(dt.datetime.today())[11:19]
    t.tracer(0)
    t1.clear()
    t1.write(time[0:2]+"时:"+time[3:5]+"分:"+time[6:8]+"秒",font=("华文琥珀",50,"normal"))
    t.update()