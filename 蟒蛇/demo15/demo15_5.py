import turtle as t
#长宽
ss=[[122,13],[134,15],[100,20],[20,5],[200,24],[70,34],[233,40]]
# 初始化画笔
X_len=600
Y_len=300
x0=-200
y0=-100
t.speed(0)
t.hideturtle()
#画坐标轴
t.penup()
t.goto(-200,-100)
t.pendown()
t.forward(600)
t.backward(600)
t.left(90)
t.forward(300)
t.right(90)
t.color("red","red")
# 画线
a=0
for i in range(len(ss)):
    #去到横坐标
    t.penup()
    t.goto(-150+i*50+a,-100)
    t.pendown()
    t.left(90)
    # 开画
    t.begin_fill()
    t.forward(ss[i][0])
    t.right(90)
    t.forward(ss[i][1])
    t.right(90)
    t.forward(ss[i][0])
    t.right(90)
    t.forward(ss[i][1])
    a+=ss[i][1]
    t.end_fill()
    t.left(180)
