import turtle as t

# 设置画布大小及笔速
t.setup(1050, 1050)


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
    t.fillcolor("red")
    if e == 1:
        t.penup()
        t.goto(a + d / 8, b + d * 5 / 4)
        t.pendown()
        t.setheading(90)
    else:
        t.penup()
        t.goto(a + d * 7 / 8, b + d / 4)
        t.pendown()
        t.setheading(270)
    t.begin_fill()
    t.circle(d * 0.414 / 10, 225)
    t.forward(d / 10)
    t.left(90)
    t.forward(d / 10)
    t.circle(d * 0.414 / 10, 225)
    t.end_fill()


# 定义数字
def num(a, b, c, d, e):
    t.pensize(5)
    t.pencolor("red")
    if e == 1:
        t.penup()
        t.goto(a + d / 10, b + d * 27 / 20)
        t.pendown()
        t.write(6, font=("", int(d / 10), "normal"))
    else:
        t.penup()
        t.goto(a + d * 17 / 20, b + d / 20)
        t.pendown()
        t.write(9, font=("", int(d / 10), "normal"))


# 打包函数画一张牌
def poke(a, b, c, d):
    cloth(a, b, c)  # 画画布
    xin(a, b, c / 2, d, 1)  # 左上角红心
    xin(a, b, c / 2, d, -1)  # 右下角红心
    num(a, b, c, d, 1)  # 左上角数字
    num(a, b, c, d, -1)  # 右下角数字
    # 画中间的红心
    xin(a + c * 3 / 16, b, c, d, 1)
    xin(a + c * 3 / 16, b - c / 2, c, d, 1)
    xin(a + c * 9 / 16, b - c / 2, c, d, 1)
    xin(a + c * 9 / 16, b, c, d, 1)
    xin(a - c * 3 / 16, b, c, d, -1)
    xin(a - c * 9 / 16, b, c, d, -1)


# 打包函数画五张牌
def pokes():
    t.tracer(False)  # 一次性画好
    for i in range(5):  # 循环五次，画五张
        poke(-500 + 200 * i, -200, 200, 200)
    t.update()  # 更新画面


# 调用pokes
pokes()
t.hideturtle()  # 隐藏笔头
t.done()
