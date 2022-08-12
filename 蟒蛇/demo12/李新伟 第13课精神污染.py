import turtle as t
import random as r
t.setup(900,900)        #设置窗口大小
t.screensize(900,900)   #设置画布大小
t1=t.Pen()              #设置画笔t1
t2=t.Pen()              #设置画笔t2
t1.hideturtle()         #隐藏画笔t1
t2.hideturtle()         #隐藏画笔t2
color=["red","orange","yellow","green","blue","black","purple"]     #设置画笔颜色为七种颜色的列表
speed=[0,8,9,10]        #设置t1的speed为0，8，9，10四个档次
baclr=["white","brown","pink","cyan","gray","khaki","skyblue"]      #设置背景颜色为七种颜色的列表

def pen_1():                    #定义t1无规则运动
    bold=r.randint(3,10)        #取画笔宽度为3到10之间的随机数
    num=r.randint(0,6)          #取num为1到7之间随机数，表示七种画笔颜色
    direct=r.randint(0,360)     #取角度为0到360之间随机数
    distance=r.randint(20,50)   #取运动距离为20到50之间随机数
    num_1=r.randint(0,3)        #num_1为0到3之间随机数

    color_1=color[num]      #根据num随机值在color中选择一种颜色
    speed_1=speed[num_1]    #根据num_1随机值在speed中选择一种速度

    x=t1.xcor()     #设置t1的x坐标为x
    y=t1.ycor()     #设置t1的y坐标为y
    if x>350 or x<-350:         #将x坐标的边界设为（-350，350）
        t1.backward(distance)   #到达边界时退后一步
    if y>350 or y<-350:         #将y坐标的边界设为（-350，350）
        t1.backward(distance)   #到达边界时退后一步
    t1.speed(speed_1)       #设置t1速度
    t1.left(direct)         #设置t1左转度数
    t1.pensize(bold)        #设置t1宽度
    t1.pencolor(color_1)    #设置t1颜色
    t1.forward(distance)    #设置t1运动距离
    
R=10                    #设置t2画圆半径
t2.speed(0)             #设置t2速度为0

def pen_2():    #定义t2有规则运动
    bold=r.randint(1,5)     #取画笔宽度为3到10之间的随机数
    num=r.randint(0,6)      #取num为1到7之间随机数，表示七种画笔颜色
    color_1=color[num]      #根据num随机值在color中选择一种颜色
    t2.pensize(bold)        #设置t2宽度
    t2.pencolor(color_1)    #设置t2颜色
    global R        #用global声明R,便于后面修改R
    t2.penup()      #抬比
    t2.goto(0,-R)   #画笔移去（0，-R）
    t2.pendown()    #落笔
    flag=0              #设置一个flag用来限定t2的半径
    t2.circle(R,360)    #将t2设置为以R为半径,(0,0)为圆心画圆
    if R>350:       #当半径大于350时flag加一
        flag+=1
    elif R<10:      #当半径小于0时flag减一
        flag-=1
    if flag==0:     #flag为0时半径增大5
        R+=5
    else:           #flag为1时半径减小5
        R-=5
        
def cloth():
    num=r.randint(0,6)      #取num为1到7之间随机数，表示七种背景颜色
    sleep=r.randint(1,2)    #取sleep为1，2
    baclr_1=baclr[num]      #根据num随机值在bgclr中选择一种背景颜色
    while(sleep>0):         #循环执行当sleep大于0时，取上面去定的颜色，并且每次循环sleep-1,直到sleep==0，以此来实现背景的不定时更替
        t.bgcolor(baclr_1)
        sleep-=1

while True:  #运用循环使画面不停运动
    pen_1()  #调用画笔1
    cloth()  #改变背景颜色
    pen_2()  #调用画笔2
    cloth()  #改变背景颜色

