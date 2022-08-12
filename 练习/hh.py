#coding=gbk
import random as r
x=r.randint(1,99)
print(x)
b=0
c=0
a=input('我想好了一个1~99的数字，你快来猜猜~(按回车退出)\n')
while(a!=''):
    for i in a:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
            c+=1
    print('11')