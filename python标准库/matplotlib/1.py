# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-1,1,50)   #从-1到1，中间有50个点连起来
y1=2**x+1
y2=x**2+1

plt.figure(num=1,figsize=(8,8))  #画布，到下一个画布之前都为这个画布的内容
plt.plot(x,y1,color="green")
plt.xlabel("I am x")  #x轴描述
plt.ylabel("I am y")

plt.figure(num=2,figsize=(8,8))
plt.plot(x,y2,color="red",linewidth=3.0,linestyle="--") #定义自变量，因变量，颜色，线宽，线的样式

plt.xlim((-1,2))  #设置x轴范围
plt.ylim((-1,3))  #设置y轴范围
new_ticks=np.linspace

plt.show()
