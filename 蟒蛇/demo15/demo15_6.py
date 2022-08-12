import turtle as t
#长宽
ss=[[122,13],[134,15],[100,20],[20,5],[200,24],[70,34]]
# 初始化画笔
X_len=500
Y_len=300
x0=-200
y0=-100
t.speed(0)
t.hideturtle()
#画坐标轴
t.penup()
t.goto(-200,-100)
t.pendown()
t.forward(500)
t.backward(500)
t.left(90)
t.forward(300)
t.right(90)
t.color("red","red")
a=0
# 画线
for i in range(len(ss)):
    # 去到横坐标
    t.penup()
    t.goto(-150+i*50+a,-100)
    t.pendown()
    t.setheading(90)
    # 画线
    for j in range(ss[i][1]):
        t.forward(ss[i][0])
        t.penup()
        t.goto(-150+i*50+a+j,-100)
        t.pendown()
    a+=ss[i][1]
