#coding=gbk
import turtle as t

# ���û����ٶȺͻ�����С
t.speed(0)
t.setup(1500, 1000)

# ��������С����ɫ
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

# ��������
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

# ����С����
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

# �ѻ����ʹ�С���Ǻ�����������Ǻ���
def flag(x, y, z):
    cloth(x, y, z)
    star1(x,y, z)
    star2(x,y, z, 40)
    star2(x,y, z, 14)
    star2(x,y, z, 348)
    star2(x, y,z, 325)

while True:
    input('�����')
# ��try��ֹ������������С����
def insert():
    try:
        x = int(input('������x����\n'))
        y = int(input('������y����\n'))
        z = int(input('��������Ǵ�С\n'))
        flag(x,y,z)
    except:
        print('�����������������')
        insert()

# ���ú���
insert()


t.hideturtle()