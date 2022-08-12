# coding=gbk
import turtle as t

# ���û�����С������
t.speed(0)
t.setup(1000, 1000)


# ���廭�� a,bΪ���½��������,cΪ������С
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


# �������  a,bΪ����,cΪ��С,dҪ��c��ȣ�eΪ����
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

# ���� a,bΪ����,cΪ��С,dҪ��c��ȣ�eΪ����,d�������Ʒ���
def tao(a, b, c, d, e):
    t.pensize(1)
    t.color("", "black")
    # ��ͼ�ε�����setheadingֵ
    z = 315
    y = 225
    x = -90
    q = 160  # ��rightֵ
    if e != 1:  # �ж�����
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

#÷�� a,bΪ����,cΪ��С,dҪ��c��ȣ�eΪ����,d�������Ʒ���
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

#����  a,bΪ����,cΪ��С,dҪ��c��ȣ�eΪ����,d��ռλ��
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

# ���������������
def pokes():
    for i in range(5):
        # ��������
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
        #��װһ�����������������ֻ�ɫ�ĺ���
        def pai(a, b, c, d, e):
            if i==0 or i==4:
                tao(a,b,c,d,e)
            elif i==1:
                xin(a,b,c,d,e)
            elif i==2:
                mei(a,b,c,d,e)
            else:
                fan(a,b,c,d,e)
        # ���������һ����
        def poke(a, b, c, d):
            cloth(a, b, c)  # ������
            num(a, b, c, d, 1)  # ���Ͻ�����
            num(a, b, c, d, -1)  # ���½�����
            pai(a, b+d/16, c/2, d, 1)  # ���Ͻ�ͼ��
            pai(a, b-d/16, c/2, d, -1)  # ���½�ͼ��
            # ���м��ͼ��
            pai(a + c * 3 / 16, b, c, d, 1)
            pai(a + c * 3 / 16, b - c * 3 / 8, c, d, 1)
            pai(a + c * 9 / 16, b - c * 3 / 8, c, d, 1)
            pai(a + c * 9 / 16, b, c, d, 1)
            pai(a - c * 3 / 16, b, c, d, -1)
            pai(a - c * 9 / 16, b, c, d, -1)
        t.tracer(False) # ���ػ�ͼ����
        poke(-500+200*i,0,200,200)
        t.update()
# ���ú���pokes
pokes()
t.hideturtle()  # ���ر�ͷ
t.done()