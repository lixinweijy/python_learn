# coding=gbk
import turtle as t

# 画画布，同时把画布打包为了不一运行程序画布就跳出来
def hh():
    t.speed(0)
    t.setup(600,900)
    t.penup()
    t.goto(-200,-300)
    t.pendown()
    t.forward(400)
    t.left(90)
    t.forward(600)
    t.left(90)
    t.forward(400)
    t.left(90)
    t.forward(600)
    t.pencolor("")

#1  x,y为位置，z为1正，否则反
def one(x,y,z,d):
    t.penup()
    t.goto(x, y)
    t.pendown()
    a=290
    b=250
    if d==1:
        d="black"
    else:
        d="red"
    t.pencolor(d)
    t.pensize(5)
    if z!= 1:
        a=360-a
        b=360-b
    t.setheading(a)
    t.forward(50)
    t.backward(50)
    t.setheading(b)
    t.forward(50)
    t.backward(25)
    t.setheading(0)
    t.forward(17)
#2  x,y为位置，z为1正，否则反
def two(x,y,z,d):
    t.pensize(5)
    if d == 1:
        d = "black"
    else:
        d = "red"
    t.pencolor(d)
    if z==1:
        t.penup()
        t.goto(x-14, y-10)
        t.pendown()
        t.setheading(90)
        t.circle(-12, 180)
        t.setheading(240)
        t.forward(40)
        t.setheading(0)
        t.forward(22)
    else:
        t.penup()
        t.goto(x+14, y+10)
        t.pendown()
        t.setheading(270)
        t.circle(-12, 180)
        t.setheading(60)
        t.forward(40)
        t.setheading(180)
        t.forward(22)
#3  x,y为位置，z为1正，否则反
def three(x, y, z,d):
    if d==1:
        d="black"
    else:
        d="red"
    t.pensize(5)
    if z == 1:
        t.penup()
        t.goto(x - 20, y - 60)
        t.pendown()
        t.write("3", font=("", 60,"normal"))
    else:
        t.penup()
        t.goto(x-50, y-20)
        t.pendown()
        t.write("ε", font=("",80,"normal"))
#4  x,y为位置，z为1正，否则反
def four(x,y,z,d):
    if d==1:
        d="black"
    else:
        d = "red"
    t.pencolor(d)
    t.pensize(5)
    if z == 1:
        t.penup()
        t.goto(x+15, y-22)
        t.pendown()
        t.setheading(180)
        t.forward(40)
        t.right(130)
        t.forward(40)
        t.setheading(270)
        t.forward(53)
    else:
        t.penup()
        t.goto(x-15, y+22)
        t.pendown()
        t.setheading(0)
        t.forward(40)
        t.right(130)
        t.forward(40)
        t.setheading(90)
        t.forward(53)
#5  x,y为位置，z为1正，否则反
def five(x,y,z,d):
    if d==1:
        d="black"
    else:
        d="red"
    t.pencolor(d)
    t.pensize(5)
    if z == 1:
        t.penup()
        t.goto(x-5, y)
        t.pendown()
        t.setheading(0)
        t.forward(15)
        t.backward(15)
        t.setheading(90)
        t.forward(5)
        t.backward(21)
        t.setheading(0)
        t.circle(-15,190)
    else:
        t.penup()
        t.goto(x-10, y)
        t.pendown()
        t.setheading(0)
        t.forward(15)
        t.setheading(270)
        t.forward(5)
        t.backward(21)
        t.setheading(180)
        t.circle(-15, 190)
#6  x,y为位置，z为1正，否则反
def six(x,y,z,d):
    if d==1:
        d="black"
    else:
        d="red"
    t.pencolor(d)
    t.pensize(5)
    if z == 1:
        t.penup()
        t.goto(x-20, y-60)
        t.pendown()
        t.write("6",font=("楷体",60,"normal"))
    else:
        t.penup()
        t.goto(x-10,y-20)
        t.pendown()
        t.write("9", font=("楷体", 60,"normal"))

#7  x,y为位置，z为1正，否则反
def seven(x,y,z,d):
    if d==1:
        d="black"
    else:
        d="red"
    t.pencolor(d)
    t.pensize(5)
    if z == 1:
        t.penup()
        t.goto(x-8, y+5)
        t.pendown()
        t.setheading(0)
        t.forward(25)
        t.right(110)
        t.forward(50)
    else:
        t.penup()
        t.goto(x+8, y-5)
        t.pendown()
        t.setheading(180)
        t.forward(25)
        t.right(110)
        t.forward(50)

#8  x,y为位置，z为1正，否则反
def eight(x,y,z,d):
    if d==1:
        d="black"
    else:
        d="red"
    t.pencolor(d)
    t.pensize(5)
    if z == 1:
        t.penup()
        t.goto(x, y-15)
        t.pendown()
        t.setheading(0)
        t.circle(12,360)
        t.circle(-15, 360)
    else:
        t.penup()
        t.goto(x, y+15)
        t.pendown()
        t.setheading(180)
        t.circle(-15, 360)
        t.circle(12, 360)

#9  x,y为位置，z为1正，否则反
def nine(x,y,z,d):
    t.penup()
    t.goto(x, y)
    t.pendown()
    if d==1:
        d="black"
    else:
        d="red"
    t.pencolor(d)
    t.pensize(5)
    if z == 1:
        t.penup()
        t.goto(x - 13, y - 60)
        t.pendown()
        t.write("9",font=("楷体",60,"normal"))
    else:
        t.penup()
        t.goto(x -22, y - 20)
        t.pendown()
        t.write("6",font=("楷体", 60,"normal"))

#10  x,y为位置，z为1正，否则反
def ten(x, y, z,d):
    if d==1:
        d="black"
    else:
        d="red"
    t.pencolor(d)
    t.pensize(5)
    if z == 1:
        t.penup()
        t.goto(x-15, y+5)
        t.pendown()
        t.setheading(270)
        t.forward(50)
        t.backward(25)
        t.penup()
        t.setheading(0)
        t.forward(11)
        t.pendown()
        t.setheading(90)
        t.forward(15)
        t.circle(-11,180)
        t.forward(30)
        t.circle(-11, 180)
        t.forward(15)
    else:
        t.penup()
        t.goto(x+15, y+43)
        t.pendown()
        t.setheading(270)
        t.forward(50)
        t.backward(25)
        t.penup()
        t.setheading(180)
        t.forward(11)
        t.pendown()
        t.setheading(90)
        t.forward(15)
        t.circle(11, 180)
        t.forward(30)
        t.circle(11, 180)
        t.forward(15)

# 黑桃
def tao(a,b,c,d,e):
    t.penup()
    t.goto(a,b)
    t.pendown()
    if d == 1:
        d = "black"
    else:
        d = "red"
    t.fillcolor(d)
    t.begin_fill()
    if e==1:
        t.setheading(315)
        t.forward(c)
        t.backward(c)
        t.setheading(225)
        t.forward(c)
        t.circle(c*0.414,225)
        t.setheading(-90)
        t.circle(c*0.414,225)
        t.end_fill()
        t.left(180)
        t.circle(-c * 0.414, 225)
        t.forward(c/5)
        t.left(180)
        t.begin_fill()
        t.circle(c,70)
        t.right(160)
        t.forward(33*c/25)
        t.right(160)
        t.circle(c,70)
        t.end_fill()
    else:
        t.setheading(45)
        t.forward(c)
        t.backward(c)
        t.setheading(135)
        t.forward(c)
        t.circle(-c * 0.414, 225)
        t.setheading(90)
        t.circle(-c * 0.414, 225)
        t.end_fill()
        t.left(180)
        t.circle(c * 0.414, 225)
        t.forward(c/5)
        t.left(180)
        t.begin_fill()
        t.circle(-c, 70)
        t.left(160)
        t.forward(33*c/25)
        t.left(160)
        t.circle(-c, 70)
        t.end_fill()

#红桃
def xin(a,b,c,d,e):
    if d == 1:
        d = "black"
    else:
        d = "red"
    t.fillcolor(d)
    t.begin_fill()
    if e==1:
        t.penup()
        t.goto(a, b-20)
        t.pendown()
        t.setheading(90)
        t.circle(c * 0.414, 225)
        t.forward(c)
        t.left(90)
        t.forward(c)
        t.circle(c * 0.414, 225)
    else:
        t.penup()
        t.goto(a, b+20)
        t.pendown()
        t.setheading(270)
        t.circle(c * 0.414, 225)
        t.forward(c)
        t.left(90)
        t.forward(c)
        t.circle(c * 0.414, 225)
    t.end_fill()

#梅花 a为横坐标，b为纵坐标，c为大小,d==1为黑色，否则为红色,e为1则为正，否则反之
def mei(a,b,c,d,e):
    if d==1:
        d="black"
    else:
        d="red"
    t.fillcolor(d)
    if e==1:
        t.penup()
        t.goto(a, b - 8 * c / 3)
        t.pendown()
        t.begin_fill()
        t.penup()
        t.setheading(90)
        t.forward(c*5/3)
        t.left(30)
        t.pendown()
        t.circle(c/2,360)
        t.end_fill()
        t.begin_fill()
        t.right(60)
        t.circle(-c/2,360)
        t.end_fill()
        t.begin_fill()
        t.right(60)
        t.circle(c/2,360)
        t.end_fill()
        t.begin_fill()
        t.right(80)
        t.forward(c*4/3)
        t.right(100)
        t.forward(c/2)
        t.right(100)
        t.forward(c*4/3)
        t.end_fill()
    else:
        t.penup()
        t.goto(a, b +8 * c / 3)
        t.pendown()
        t.begin_fill()
        t.penup()
        t.setheading(270)
        t.forward(c * 5 / 3)
        t.left(30)
        t.pendown()
        t.circle(c/2, 360)
        t.end_fill()
        t.begin_fill()
        t.right(60)
        t.circle(-c/2, 360)
        t.end_fill()
        t.begin_fill()
        t.right(60)
        t.circle(c/2, 360)
        t.end_fill()
        t.begin_fill()
        t.right(80)
        t.forward(c * 4 / 3)
        t.right(100)
        t.forward(c/2)
        t.right(100)
        t.forward(c *4/ 3)
        t.end_fill()

#方块 a为横坐标，b为纵坐标，c为大小,d==1为黑色，否则为红色
def fan(a,b,c,d,e):
    t.penup()
    t.goto(a,b)
    t.pendown()
    if d==1:
        d="black"
    else:
        d="red"
    t.fillcolor(d)
    t.begin_fill()
    if e==1:
        t.setheading(300)
        t.forward(c*6/5)
        t.right(60)
        t.forward(c*6/5)
        t.right(120)
        t.forward(c*6/5)
        t.right(60)
        t.forward(c*6/5)
    else:
        t.setheading(60)
        t.forward(c * 6 / 5)
        t.left(60)
        t.forward(c * 6 / 5)
        t.left(120)
        t.forward(c * 6 / 5)
        t.left(60)
        t.forward(c * 6 / 5)
    t.end_fill()
# 后面判断颜色的信号量
d=0
# 每个数字里面各个元素的坐标
one_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0], [0, 90, 100, d, 1]]
two_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[0, 260, 40, d, 1],[0,-260,40, d, -1]]
three_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[0, 260,40, d, 1],[0,-260,40, d, -1],[0,48,40, d, 1]]
four_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[-70, 260,40, d, 1],[70,-260,40, d, -1],[70,260, 40, d, 1],[-70,-260, 40, d, -1]]
five_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[-70, 260,40, d, 1],[70,-260,40, d, -1],[70,260, 40, d, 1],[-70,-260, 40, d, -1],[0, 40,40, d, 1]]
six_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[-70, 260, 40, d, 1],[70,-260,40, d, -1],[70,260, 40, d, 1],[-70,-260,40, d, -1],[-70, 40,40, d, 1],[70, 40, 40, d, 1]]
seven_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[-70, 260,40, d, 1],[70,-260,40, d, -1],[70,260,40, d, 1],[-70,-260,40, d, -1],[-70, 40,40, d, 1],[70, 40,40, d, 1],[0,150,40,d,1]]
eight_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[-70, 260,40, d, 1],[70,-260,40, d, -1],[70,260,40, d, 1],[-70,-260,40, d, -1],[-70, 40,40, d, 1],[70, 40,40, d, 1],[0,150,40,d,1],[0,-150,40,d,-1]]
nine_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[-70, 260, 40, d, 1],[70,-260,40, d, -1],[70,260, 40, d, 1],[-70,-260,40, d, -1],[-70, 110,40, d, 1],[70, -110, 40, d,- 1],[-70, -110,40, d,-1],[70,110, 40, d,1],[0, 40,40, d, 1]]
ten_1=[[-150, 290, 1, d], [150, -290, 0, d], [-150, 240, 30, d, 1], [150, -240, 30, d, 0],[-70, 260, 40, d, 1],[70,-260,40, d, -1],[70,260, 40, d, 1],[-70,-260,40, d, -1],[-70, 110,40, d, 1],[70, -110, 40, d,- 1],[-70, -110,40, d,-1],[70, 110, 40, d,1],[0,180,40, d, 1],[0,-180,40, d, -1]]
# 每种花色的各个数字
black_t=[one_1,two_1,three_1,four_1,five_1,six_1,seven_1,eight_1,nine_1,ten_1]
red_t=[one_1,two_1,three_1,four_1,five_1,six_1,seven_1,eight_1,nine_1,ten_1]
plum=[one_1,two_1,three_1,four_1,five_1,six_1,seven_1,eight_1,nine_1,ten_1]
block=[one_1,two_1,three_1,four_1,five_1,six_1,seven_1,eight_1,nine_1,ten_1]
#整副扑克牌
pokes=[black_t,red_t,plum,block]
# 将发牌程序打包
def pokes_1():
    color = int(input("请输入你想要的花色\n【1】黑桃  【2】红桃  【3】梅花  【4】方块\n")) - 1
    num_1 = int(input("请输入点数（1~10）\n"))-1
    hh()
    global d
    for i in range(len(pokes[color][num_1])):
        if color == 0:
            d = 1
            def pai(a, b, c, d, e):
                tao(a, b, c, d, e)
        elif color == 1:
            def pai(a, b, c, d, e):
                xin(a, b, c, d, e)
        elif color == 2:
            d = 1
            def pai(a, b, c, d, e):
                mei(a, b, c, d, e)
        else:
            def pai(a, b, c, d, e):
                fan(a, b, c, d, e)

        if i < 2:
            x = pokes[color][num_1][i][0]
            y = pokes[color][num_1][i][1]
            z = pokes[color][num_1][i][2]
            if num_1 == 0:
                one(x, y, z, d)
            elif num_1 == 1:
                two(x, y, z, d)
            elif num_1 == 2:
                three(x, y, z, d)
            elif num_1 == 3:
                four(x, y, z, d)
            elif num_1 == 4:
                five(x, y, z, d)
            elif num_1 == 5:
                six(x, y, z, d)
            elif num_1 == 6:
                seven(x, y, z, d)
            elif num_1 == 7:
                eight(x, y, z, d)
            elif num_1 == 8:
                nine(x, y, z, d)
            elif num_1 == 9:
                ten(x, y, z, d)
        elif i < 4:
            a = pokes[color][num_1][i][0]
            b = pokes[color][num_1][i][1]
            c = pokes[color][num_1][i][2]
            e = pokes[color][num_1][i][4]
            pai(a, b, c, d, e)
        else:
            a = pokes[color][num_1][i][0]
            b = pokes[color][num_1][i][1]
            c = pokes[color][num_1][i][2]
            e = pokes[color][num_1][i][4]
            pai(a, b, c, d, e)
    t.hideturtle()
    t.done()
pokes_1()
print("发牌结束")