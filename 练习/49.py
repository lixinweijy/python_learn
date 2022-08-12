# -*- coding:utf-8 -*-
# 任务六（2）：自动获取当前时间和星期（中文）


import turtle as t
import datetime as dt
import time

# data=[2,0,2,2,10,0,2,10,2,8]
data2 = []
shape = [[0, 1, 1, 1, 1, 1, 1, '0'], [0, 1, 0, 0, 0, 0, 1, '1'], [1, 0, 1, 1, 0, 1, 1, '2'], [1, 1, 1, 0, 0, 1, 1, '3'],
         [1, 1, 0, 0, 1, 0, 1, '4'] \
    , [1, 1, 1, 0, 1, 1, 0, '5'], [1, 1, 1, 1, 1, 1, 0, '6'], [0, 1, 0, 0, 0, 1, 1, '7'], [1, 1, 1, 1, 1, 1, 1, '8'] \
    , [1, 1, 1, 0, 1, 1, 1, '9'], [1, 0, 0, 0, 0, 0, 0, '-'], [0, 0, 0, 0, 0, 0, 0, ' ']]
week = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']


# 一个笔画
def drawline(bh):
    t.penup()
    t.forward(9)
    t.pendown() if bh == 1 else t.penup()
    t.forward(30)
    t.penup()
    t.forward(5)
    t.right(90)


# 一个数字
def drawNum(num):
    for i in range(7):
        drawline(shape[num][i])
        if i == 3:
            t.left(90)
    t.setheading(0)
    t.penup()
    t.forward(15)


# 动态获取时间,添加到日期列表中
#
# print(tm)
# print(str(tm)[0:19])

def time_list(tm):
    for i in str(tm)[0:19]:
        if i == '-':
            i = 10
            data2.append(i)
        elif i == ' ':
            i = 11
            data2.append(i)
        elif i == ':':
            i = 12
            data2.append(i)
        else:
            i = int(i)
            data2.append(i)


def show(tm):
    time_list(tm)
    t.penup()
    t.goto(-600, 200)
    t.pendown()
    for i in data2:
        if i == 12:
            t.penup()
            t.goto(t.xcor() + 20, t.ycor() - 30)
            t.pendown()
            t.write(':', align='center', font=('宋体', 50, 'bold'))
            t.penup()
            t.goto(t.xcor() + 10, t.ycor() + 30)
            t.pendown()
        else:
            drawNum(i)
    # 显示当前星期
    t1 = t.Pen()
    t1.penup()
    t1.goto(50, 0)
    t1.pendown()
    t1.write(week[tm.weekday()], align='center', font=('宋体', 50, 'bold'))
    t1.hideturtle()


def main():
    t.setup(1200, 600)
    t.pensize(5)
    while True:
        tm = dt.datetime.today()
        t.tracer(0)
        t.clear()
        show(tm)
        t.update()
        print(tm)


if __name__ == '__main__':
    main()

