#coding=gbk
import turtle as t
# 设置画布大小
t.setup(1000, 1000)
# 定义画布 a,b为左下角起点坐标,c为画布大小
def cloth(a, b, c):
    t.setheading(0)  # 重置画笔方向
    t.pensize(1)  # 重置画笔大小
    t.color("black", "white")  # 重置画笔颜色及填充颜色，将画布设置为白色便于后期遮盖卡牌
    t.penup()
    t.goto(a, b)
    t.pendown()
    t.begin_fill()
    t.forward(c)
    t.left(90)
    t.forward(3 * c / 2)
    t.left(90)
    t.forward(c)
    t.left(90)
    t.forward(3 * c / 2)
    t.end_fill()
    t.pencolor("")

# 定义红心  a,b为坐标,c为大小,d要与c相等，e为正反
def xin(a, b, c):
    t.fillcolor("red")
    t.begin_fill()
    t.penup()
    t.goto(a + c/ 8, b + c * 5 / 4)
    t.pendown()
    t.setheading(90)
    t.circle(c * 0.414 / 10, 225)
    t.forward(c / 10)
    t.left(90)
    t.forward(c / 10)
    t.circle(c * 0.414 / 10, 225)
    t.end_fill()

# 黑桃 a,b为坐标,c为大小,d要与c相等，e为正反,d用来控制方向
def tao(a, b, c):
    t.pensize(1)
    t.color("", "black")
    t.penup()
    t.goto(a + c/ 8, b + c* 21/16)
    t.pendown()
    t.setheading(315)
    t.begin_fill()
    t.forward(c/10)
    t.backward(c/10)
    t.setheading(225)
    t.forward(c/10)
    t.circle(c*0.414/10, 225)
    t.setheading(-90)
    t.circle(c*0.414/10, 225)
    t.end_fill()
    t.left(180)
    t.circle(-c* 0.414/10, 225)
    t.forward(c/50)
    t.left(180)
    t.begin_fill()
    t.circle(c/10, 70)
    t.right(160)
    t.forward(33*c/250)
    t.right(160)
    t.circle(c/10, 70)
    t.end_fill()

#梅花 a,b为坐标,c为大小,d要与c相等，e为正反,d用来控制方向
def mei(a,b,c):
    t.pensize(1)
    t.color("", "black")
    t.penup()
    t.goto(a + c/ 8, b + c* 21/16)
    t.pendown()
    t.begin_fill()
    t.penup()
    t.setheading(270)
    t.forward(c*2/25)
    t.left(210)
    t.pendown()
    t.circle(c/25,360)
    t.end_fill()
    t.begin_fill()
    t.right(60)
    t.circle(-c/25,360)
    t.end_fill()
    t.begin_fill()
    t.left(120)
    t.circle(-c/25,360)
    t.end_fill()
    t.begin_fill()
    t.left(80)
    t.forward(c*8/75)
    t.left(100)
    t.forward(c/25)
    t.left(100)
    t.forward(c*8/75)
    t.end_fill()

#方块  a,b为坐标,c为大小,d要与c相等，e为正反,d用占位置
def fan(a,b,c):
    t.pensize(1)
    t.color("","red")
    t.penup()
    t.goto(a + c/ 8, b + c*21/16)
    t.pendown()
    t.begin_fill()
    t.setheading(300)
    t.forward(c/10)
    t.right(60)
    t.forward(c/10)
    t.right(120)
    t.forward(c/10)
    t.right(60)
    t.forward(c/10)
    t.end_fill()
i=0 #为防止num报错，取i=0
# 定义数字
def num(a, b, c,i):
    t.pencolor("red")
    t.pensize(5)
    if i%2==0:
        t.pencolor("black")
    if i ==0:
        z="J"
    elif i ==1:
        z="Q"
    elif i ==2:
        z="K"
    elif i ==5:
        z="A"
    else:
        z="J\nO\nK\nE\nR"
        b-=c/8
        c=4*c/5
    t.penup()
    t.goto(a + c / 10, b + c * 27 / 20)
    t.pendown()
    t.write(z, font=("", int(c / 10), "normal"))
# 打包函数画一张牌
def poke(a, b, c ,i):
    cloth(a, b, c)  # 画画布
    if i ==0:
        tao(a,b,c)  # 左上角红心
    elif i==1:
        xin(a, b, c)
    elif i==2:
        mei(a,b,c)
    elif i==5:
        fan(a, b, c)
    num(a, b, c,i)  # 左上角数字
    # 画中间的红心
    t.pencolor("red")
    fan(a + c/11, b-c*7/2, c*7/2)

# 打包函数画五张牌
def pokes():
    t.tracer(False)  # 一次性画好
    for i in range(6):  # 循环六次，画六张
        poke(-200 + 40 * i, -200, 200,i)
    t.update()
    # 更新画面

# 调用pokes
pokes()
# 隐藏画笔
t.hideturtle()
t.done()