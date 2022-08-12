#coding=gbk
import matplotlib.pyplot as mp#�����
import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-3,3,50)#����x�ķ�Χ����ĸ���
y1=2*x+1  #��������֮���ϵ
y2=x**2+1

mp.figure(num=1,figsize=(10,8)) #����һ��ͼ�񣬿ɶඨ�弸��,ͼ�����ִ���ͳ���ɵ�
mp.plot(x,y1) #��x��y1���һ��ͼ��
mp.plot(x,y2,color='red',linewidth=1.0,linestyle='--')#�ɶ����ߵ���ɫ����ȣ�����

mp.xlim((-1,2))#����x��Χ
mp.ylim((-2.3))#����y2��Χ
mp.xlabel('x')#����x������
mp.ylabel('y')#����y������

new_ticket=np.linspace(-1,2,5)
print(new_ticket)
mp.xticks(new_ticket)
plt.yticks()


mp.show()