#coding=gbk
import turtle as t
import random as r
t.setup(900,900)
t.screensize(900,900)
#������֧����
t1=t.Pen()
t2=t.Pen()
t3=t.Pen()
t4=t.Pen()
#��ʼ�����ʵ���ɫ���ٶȣ�λ��
def initial():
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t4.hideturtle()
    t1.speed(0)
    t2.speed(0)
    t1.color("green","green")
    t2.color("green","green")
    t3.penup()
    t3.goto(25,200)
    t3.pendown()
    t4.penup()
    t4.goto(-20,200)
    t4.pendown()
#���������״���
def frame():
    t1.penup()
    t1.goto(100,0)
    t1.pendown()
    t1.left(90)
    t1.forward(396)
    t1.left(90)
    t1.forward(95)
    t1.right(90)
    t1.forward(15)
    t1.left(90)
    t1.forward(10)
    t1.left(90)
    t1.forward(15)
    t1.right(90)
    t1.forward(95)
    t1.left(90)
    t1.forward(396)
    t1.left(90)
    t1.forward(200)
    t1.left(90)
#�������ӵĵ���
def block(a):
    if a<100:
        t1.begin_fill()
        t1.forward(4)
        t1.left(90)
        t1.pencolor("white")
        if a == 99:
            t1.pencolor("green")
        t1.forward(200)
        t1.pencolor("green")
        t1.left(90)
        t1.forward(4)
        t1.left(90)
        t1.forward(200)
        t1.end_fill()
        t1.left(90)
        t1.forward(4)
    else: #���ٷ�֮�ٵ����Ҫ��һ�ֻ���
        t1.begin_fill()
        t1.left(90)
        t1.forward(95)
        t1.right(90)
        t1.forward(15)
        t1.left(90)
        t1.forward(10)
        t1.left(90)
        t1.forward(15)
        t1.left(90)
        t1.forward(10)
        t1.end_fill()
#����ԲȦ
def t2_pen(q):
    #ԲȦ�ĺ���������-100��100�ڱ仯��
    x=r.randint(-100,100)
    t2.penup()
    t2.clear() #ÿ����һ��ԲȦ�����һ��ԲȦ
    t2.goto(x,q*20-300)  #ԲȦ��������
    t2.begin_fill()
    t2.circle(q,360)
    t2.end_fill()
a=0  #������¼��ص���
q=5  #����ʵ��ԲȦ����
#׼������
initial()
frame()
while(a<100):
    a+=1
    q+=1
    if q==15:
        q=5
    t2_pen(q)  #��ԲȦ
    t4.clear()
    t4.write(a, font=("��������", 20, "normal"))  #������
    t3.write("%", font=("���Ĳ���", 20, "normal")) #���ٷֺ�
    block(a)  #���ӵ���