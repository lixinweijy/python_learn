import turtle as t
#设置画布大小
t.setup(1000,1000)

#定义画布 a,b为左下角起点坐标,c为画布大小
def cloth(a,b,c):
    t.setheading(0) #重置画笔方向
    t.pensize(1)   #重置画笔大小
    t.color("black","white")  #重置画笔颜色及填充颜色，将画布设置为白色便于后期遮盖卡牌
    t.penup()
    t.goto(a,b)
    t.pendown()
    t.begin_fill()
    t.forward(c)
    t.left(90)
    t.forward(3*c/2)
    t.left(90)
    t.forward(c)
    t.left(90)
    t.forward(3*c/2)
    t.end_fill()
    t.pencolor("")
    
#定义红心  a,b为坐标,c为大小,d要与c相等，e为正反
def xin(a,b,c,d,e):
    t.fillcolor("red")
    t.begin_fill()
    if e==1:
        t.penup()
        t.goto(a+d/8, b+d*5/4)
        t.pendown()
        t.setheading(90)
    else:
        t.penup()
        t.goto(a+d*7/8,b+d/4)
        t.pendown()
        t.setheading(270)
    t.circle(c* 0.414/10, 225)
    t.forward(c/10)
    t.left(90)
    t.forward(c/10)
    t.circle(c* 0.414/10, 225)
    t.end_fill()

#定义数字
def num(a,b,c,d,e):
    t.pensize(5)
    t.pencolor("red")
    if e==1:
        t.penup()
        t.goto(a+d/10, b+d*27/20)
        t.pendown()
        t.write(6,font=("",int(c/10), "normal"))
    else:
        t.penup()
        t.goto(a+d*17/20,b+d/20)
        t.pendown()
        t.write(9,font=("",int(c/10), "normal"))
#打包函数画一张牌
def poke(a,b,c,d):
    cloth(a,b,c)#画画布
    xin(a,b,c,d,1)#左上角红心
    num(a,b,c,d,1)#左上角数字
    #画中间的红心
    xin(a+c*3/8,b-c/2,7*c/2,d,1)
#打包函数画五张牌
def pokes():
    t.tracer(False) #一次性画好
    for i in range(5):  # 循环五次，画五张
        poke(-200+ 40 * i, -200, 200, 200)
    t.update()#更新画面

#调用pokes
pokes()
# 隐藏画笔
t.hideturtle()
t.done()
