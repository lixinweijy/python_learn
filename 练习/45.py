# -*- coding:utf-8 -*-
import turtle as t
import serial
ser = serial.Serial('COM3', 9600, timeout=1)
t1=t.Pen()
t2=t.Pen()
t1.hideturtle()
t2.hideturtle()
t1.pencolor("black")
t2.pencolor("gray")
z=''
flag=0
while 1:
    a=ser.readline().decode("utf-8")
    a=str.strip(a)
    if a!='' and a!='=':
        flag+=1
        z+=a
        t1
        t1.write(flag,)


