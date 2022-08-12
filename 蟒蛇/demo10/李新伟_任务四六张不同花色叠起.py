#coding=gbk
import turtle as t
# ���û�����С
t.setup(1000, 1000)
# ���廭�� a,bΪ���½��������,cΪ������С
def cloth(a, b, c):
    t.setheading(0)  # ���û��ʷ���
    t.pensize(1)  # ���û��ʴ�С
    t.color("black", "white")  # ���û�����ɫ�������ɫ������������Ϊ��ɫ���ں����ڸǿ���
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

# �������  a,bΪ����,cΪ��С,dҪ��c��ȣ�eΪ����
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

# ���� a,bΪ����,cΪ��С,dҪ��c��ȣ�eΪ����,d�������Ʒ���
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

#÷�� a,bΪ����,cΪ��С,dҪ��c��ȣ�eΪ����,d�������Ʒ���
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

#����  a,bΪ����,cΪ��С,dҪ��c��ȣ�eΪ����,d��ռλ��
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
i=0 #Ϊ��ֹnum����ȡi=0
# ��������
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
# ���������һ����
def poke(a, b, c ,i):
    cloth(a, b, c)  # ������
    if i ==0:
        tao(a,b,c)  # ���ϽǺ���
    elif i==1:
        xin(a, b, c)
    elif i==2:
        mei(a,b,c)
    elif i==5:
        fan(a, b, c)
    num(a, b, c,i)  # ���Ͻ�����
    # ���м�ĺ���
    t.pencolor("red")
    fan(a + c/11, b-c*7/2, c*7/2)

# ���������������
def pokes():
    t.tracer(False)  # һ���Ի���
    for i in range(6):  # ѭ�����Σ�������
        poke(-200 + 40 * i, -200, 200,i)
    t.update()
    # ���»���

# ����pokes
pokes()
# ���ػ���
t.hideturtle()
t.done()