#coding=gbk
import random as r
x=r.randint(1,99)
print(x)
b=0
c=0
flag=0
a=input('我想好了一个1~99的数字，你快来猜猜~(按回车退出)\n')
while(a!=''):
    for i in a:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
            c+=1
    if(c==0):
        # a = eval(a)
        while(b<8):
            b+=1
            try:
                a=eval(a)
            except:
                break
            if(x==a):
                flag=1
                break
            elif(a<1 or a>99):
                print('超出范围了哟~')
                a=input('请重新输入吧~(按回车退出)\n')
            elif(x>a):
                print('你猜小了')
                a=input('继续猜猜~(按回车退出)\n')
            elif(x<a):
                print('猜大了哟')
                a=input('继续猜猜~(按回车退出)\n')
        if flag!=1:
            try:
                a = eval(a)
            except:
                continue
        if(b<5):
            print('你猜了{}次就猜中了'.format(b))
            print('你真是天才！')
        elif(b<7):
            print('你猜了{}次就猜中了'.format(b))
            print('你太聪明了！')
        elif(b<8):
            print('你猜了{}次就猜中了'.format(b))
            print('还不错哦~')
        elif(b==8):
            print('继续加油哦~')
    else:
        print('您输入错误，应当输入纯数字。')
        a=input('继续猜猜~(按回车退出)\n')
        c=0
        continue
    c=0
    x=r.randint(1,99)
    print()
    print(x)
    a=input('我又想好了一个1~99的数字，再猜一猜吧~(按回车退出)\n')
    b=0
