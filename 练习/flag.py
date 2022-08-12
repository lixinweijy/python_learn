#coding=gbk
import turtle as t

# 设置画笔速度和画布大小
t.speed(0)
t.setup(1500, 1000)

# 定义红旗大小和颜色
def cloth(x, y, z):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('white', 'red')
    t.begin_fill()
    t.forward(300 * z)
    t.left(90)
    t.forward(200 * z)
    t.left(90)
    t.forward(300 * z)
    t.left(90)
    t.forward(200 * z)
    t.end_fill()

# 定义大红星
def star1(x, y,z):
    t.setheading(0)
    t.penup()
    t.goto(x + 10 *  z, y - 10 * z)
    t.pendown()
    t.color('', 'yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(50 * z)
        t.right(144)
    t.end_fill()

# 定义小红星
def star2(x,y, z, w):
    a = x + 60 * z
    t.setheading(w)
    t.penup()
    t.goto(a / 2, y - 16 * z)
    t.forward(50 * z)
    t.pendown()
    t.color('', 'yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(50 * z / 3)
        t.right(144)
    t.end_fill()

# 把画布和大小星星合起来变成五星红旗
def flag(x, y, z):
    cloth(x, y, z)
    star1(x,y, z)
    star2(x,y, z, 40)
    star2(x,y, z, 14)
    star2(x,y, z, 348)
    star2(x, y,z, 325)

while True:
    input('随便输')
# 用try防止输入的坐标与大小出错
def insert():
    try:
        x = int(input('请输入x坐标\n'))
        y = int(input('请输入y坐标\n'))
        z = int(input('请输入大星大小\n'))
        flag(x,y,z)
    except:
        print('输入错误，请输入整数')
        insert()

# 调用函数
insert()


t.hideturtle()