import turtle as t

# 定义红旗大小和颜色
def cloth(x, y, z):
    t.speed(0)
    t.setup(900,900)
    t.penup()
    t.setheading(0)
    t.goto(x, y)
    t.pendown()
    t.color('white', 'red')
    t.begin_fill()
    t.forward(z)
    t.right(90)
    t.forward(2*z/3)
    t.right(90)
    t.forward(z)
    t.right(90)
    t.forward(2*z/3)
    t.end_fill()

# 定义大红星
def star1(x, y,z):
    t.setheading(0)
    t.penup()
    t.goto(x + z/15, y -z/8)
    t.pendown()
    t.color('', 'yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(z/6)
        t.right(144)
    t.end_fill()

# 定义小红星
def star2(x,y, z, w):
    t.setheading(w)
    t.penup()
    t.goto(x +2*z/15 , y -8*z/50)
    t.forward(z/5)
    t.pendown()
    t.color('', 'yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(z / 18)
        t.right(144)
    t.end_fill()

# 把画布和大小星星合起来变成五星红旗
def flag(x, y, z):
    cloth(x, y, z)
    star1(x,y, z)
    star2(x,y, z,35)
    star2(x,y, z,12)
    star2(x,y, z,349)
    star2(x, y,z,325)
    t.hideturtle()

# 用try防止输入的坐标与大小出错
def insert():
    try:
        x = int(input('请输入x坐标，要属于（-450，0）之间\n'))
        y = int(input('请输入y坐标，要属于（0,300） \n'))
        z = int(input('请输入国旗大小（0，450）\n'))
        flag(x,y,z)
    except:
        b=print('输入错误，请输入整数）\n')
        insert()
        
# 循环调用函数
a=input('准备发车，若输入n则退出，否则开始\n')
while (a!= 'n'):
    insert()
    a=input('再来一次吗，若输入n则退出，否则继续\n')

print('over')

