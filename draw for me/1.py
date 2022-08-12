#coding=gbk
import matplotlib.pyplot as mp#导入包
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)#设置x的范围及点的个数
y1=2*x+1  #描述函数之间关系
y2=x**2+1

mp.figure(num=1,figsize=(10,8)) #定义一个图像，可多定义几个,图像数字代码和长宽可调
mp.plot(x,y1) #用x与y1组成一个图像
mp.plot(x,y2,color='red',linewidth=1.0,linestyle='--')#可定义线的颜色，宽度，类型

mp.xlim((-1,2))#限制x范围
mp.ylim((-2.3))#限制y2范围
mp.xlabel('x')#定义x轴名称
mp.ylabel('y')#定义y轴名称

new_ticket=np.linspace(-1,2,5)
print(new_ticket)
mp.xticks(new_ticket)
plt.yticks()


mp.show()