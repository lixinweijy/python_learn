# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
import serial
ser = serial.Serial('COM3', 9600, timeout=1)
s=[[-275,175],[-125,175],[25,175],[175,175],
   [-275,25],[-125,25],[25,25],[175,25],
   [-275,-125],[-125,-125],[25,-125],[175,-125],
   [-275,-275],[-125,-275],[25,-275],[175,-275]]
ss=[
    '1','2','3','+',
    '4','5','6','-',
    '7','8','9','*',
    'C','0','=','/'
]
c=0
b=''
while 1:
    a=ser.readline().decode("utf-8")
    a=str.strip(a)
    if a!='':
        for i in range(16):
            if a==ss[i]:
                c=i
                if i==14:
                    flag_2=1
                    break
                b+=a
        ser.write(b)
        b=''
        flag_2=0