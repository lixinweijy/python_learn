# coding=gbk
import turtle as t

# 设置画布大小及笔速
t.speed(0)
t.setup(1000, 1000)


# 定义画布 a,b为左下角起点坐标,c为画布大小
def cloth(a, b, c):
    t.setheading(0)
    t.pensize(1)
    t.pencolor("black")
    t.penup()
    t.goto(a, b)
    t.pendown()
    t.forward(c)
    t.left(90)
    t.forward(3 * c / 2)
    t.left(90)
    t.forward(c)
    t.left(90)
    t.forward(3 * c / 2)
    t.pencolor("")


# 定义红心  a,b为坐标,c为大小,d要与c相等，e为正反
def xin(a, b, c, d, e):
    t.pensize(1)
    t.color("", "red")
    if e == 1:
        t.penup()
        t.goto(a + d / 8, b + d * 19 / 16)
        t.pendown()
        t.setheading(90)
    else:
        t.penup()
        t.goto(a + d * 7 / 8, b + d * 5 / 16)
        t.pendown()
        t.setheading(270)
    t.begin_fill()
    t.circle(c * 0.414 / 10, 225)
    t.forward(c / 10)
    t.left(90)
    t.forward(c / 10)
    t.circle(c * 0.414 / 10, 225)
    t.end_fill()

# 黑桃 a,b为坐标,c为大小,d要与c相等，e为正反,d用来控制方向
def tao(a, b, c, d, e):
    t.pensize(1)
    t.color("", "black")
    # 正图形的三个setheading值
    z = 315
    y = 225
    x = -90
    q = 160  # 正right值
    if e != 1:  # 判断正反
        z = 360-z
        y = 360-y
        x = -x
        q = 360-q
        t.penup()
        t.goto(a + d * 7 / 8, b + d / 4)
        d = -d
        t.pendown()
        if -d!=c:
            d=d/2
    else:
        t.penup()
        t.goto(a + d / 8, b + d * 5 / 4)
        t.pendown()
        if d!=c:
            d=d/2
    t.setheading(z)
    t.begin_fill()
    t.forward(c/10)
    t.backward(c/10)
    t.setheading(y)
    t.forward(c/10)
    t.circle(d*0.414/10, 225)
    t.setheading(x)
    t.circle(d*0.414/10, 225)
    t.end_fill()
    t.left(180)
    t.circle(-d * 0.414/10, 225)
    t.forward(c/50)
    t.left(180)
    t.begin_fill()
    t.circle(d/10, 70)
    t.right(q)
    t.forward(33*c/250)
    t.right(q)
    t.circle(d/10, 70)
    t.end_fill()

#梅花 a,b为坐标,c为大小,d要与c相等，e为正反,d用来控制方向
def mei(a,b,c,d,e):
    t.pensize(1)
    t.color("", "black")
    x=270
    if e!=1:
        x=360-x
        t.penup()
        t.goto(a + d * 7 / 8, b + d / 4)
        d = -d
        t.pendown()
    else:
        t.penup()
        t.goto(a + d / 8, b + d * 5 / 4)
        t.pendown()
    t.begin_fill()
    t.penup()
    t.setheading(x)
    t.forward(c/10)
    t.left(210)
    t.pendown()
    t.circle(c/20,360)
    t.end_fill()
    t.begin_fill()
    t.right(60)
    t.circle(-c/20,360)
    t.end_fill()
    t.begin_fill()
    t.left(120)
    t.circle(-c/20,360)
    t.end_fill()
    t.begin_fill()
    t.left(80)
    t.forward(c*2/15)
    t.left(100)
    t.forward(c/20)
    t.left(100)
    t.forward(c*2/15)
    t.end_fill()

#方块  a,b为坐标,c为大小,d要与c相等，e为正反,d用占位置
def fan(a,b,c,d,e):
    t.pensize(1)
    t.color("","red")
    x=300
    y=120
    z=60
    if e!=1:
        z=360-z
        y=360-y
        x=360-x
        t.penup()
        t.goto(a + d * 7 / 8, b + d / 4)
        t.pendown()
    else:
        t.penup()
        t.goto(a + d / 8, b + d * 5 / 4)
        t.pendown()
    t.begin_fill()
    t.setheading(x)
    t.forward(c*3/25)
    t.right(z)
    t.forward(c*3/25)
    t.right(y)
    t.forward(c*3/25)
    t.right(z)
    t.forward(c*3/25)
    t.end_fill()

# 打包函数画五张牌
def pokes():
    for i in range(5):
        # 定义数字
        def num(a, b, c, d, e):
            t.pensize(5)
            if i == 0 or i == 2 or i==4:
                z = "black"
            else:
                z = "red"
            t.pencolor(z)
            if e == 1:
                t.penup()
                t.goto(a + d / 10, b + d * 27 / 20)
                t.pendown()
                t.write(6, font=("", int(c / 10), "normal"))
            else:
                t.penup()
                t.goto(a + d * 17 / 20, b + d / 20)
                t.pendown()
                t.write(9, font=("", int(c / 10), "normal"))
        #封装一个函数用来代替四种花色的函数
        def pai(a, b, c, d, e):
            if i==0 or i==4:
                tao(a,b,c,d,e)
            elif i==1:
                xin(a,b,c,d,e)
            elif i==2:
                mei(a,b,c,d,e)
            else:
                fan(a,b,c,d,e)
        # 打包函数画一张牌
        def poke(a, b, c, d):
            cloth(a, b, c)  # 画画布
            num(a, b, c, d, 1)  # 左上角数字
            num(a, b, c, d, -1)  # 右下角数字
            pai(a, b+d/16, c/2, d, 1)  # 左上角图案
            pai(a, b-d/16, c/2, d, -1)  # 右下角图案
            # 画中间的图案
            pai(a + c * 3 / 16, b, c, d, 1)
            pai(a + c * 3 / 16, b - c * 3 / 8, c, d, 1)
            pai(a + c * 9 / 16, b - c * 3 / 8, c, d, 1)
            pai(a + c * 9 / 16, b, c, d, 1)
            pai(a - c * 3 / 16, b, c, d, -1)
            pai(a - c * 9 / 16, b, c, d, -1)
        t.tracer(False) # 隐藏画图过程
        poke(-500+200*i,0,200,200)
        t.update()
# 调用函数pokes
pokes()
t.hideturtle()  # 隐藏笔头
t.done()