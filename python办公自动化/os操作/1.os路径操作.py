# -*- coding:utf-8 -*-
import os
print(os.getcwd())  #获取当前路径
print(os.path.join("C:\\user","path"))  #连接路径

#listdir()
print(os.listdir())  #不传参时，默认获取当前路径下的所有文件
for i in os.listdir():
    print(i,  type(i),  len(i))

print("\n\n")
lst=os.listdir("D:\\桌面\\key\\蟒蛇\\demo19")  #传入参数时，获取参数地址下的所有文件
for i in lst:
    print(i,  type(i),  len(i))

print("\n\n")
#要退到上一级..
lst1=os.listdir('../os操作')
for i in lst1:
    print(i, type(i), len(i))

print("\n\n")
#scandir
lst2=os.scandir()
for i in lst2:
    print(i,type(i),i.name)
#区别:listdir是字符串，scandir是文件
#所以listdir更方便看，scandir更方便操作
