# -*- coding:utf-8 -*-
import serial
import turtle as t
ser = serial.Serial('COM3', 9600, timeout=1)
t.hideturtle()
t.penup()
t.goto(-150,0)
t.pendown()
while 1:
    a=ser.readline().decode("utf-8")
    t.tracer(0)
    t.clear()
    t.write("电压(v):"+a,font=("",30,"normal"))
    t.update()
