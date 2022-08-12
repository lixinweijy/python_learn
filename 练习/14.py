#coding=gbk
import random as r
x=r.randint(1,99)
print(x)
b=0
def hhh():
        while(1):
            try:
                global a
                a = eval(a)
                break
            except:
                print('输入错误，应该输入1~99的纯整数')
                a = input('再输入一次吧~\n')
                continue
a=0
while(a!=""):
        while(b<9):
            if b==0:
                a = input('我想好了一个1~99的整数，你快来猜~(按回车退出)\n')
            else:
                a=input()
            hhh()
            b+=1
            print("您已输入{}次".format(b))
            if(x==a):
                break
            elif(a<1 or a>99):
                print('超出范围啦，请输入一个1~99的整数')
            elif(x>a):
                print('你猜小了')
            elif(x<a):
                print('猜大了哟')

        if(x==a):
                print('你猜对啦~')
        if(b<6):
            print('你猜了{}次就猜中了'.format(b))
            print('你真是天才！\n')
        elif(b<7):
            print('你猜了{}次就猜中了'.format(b))
            print('你太聪明了！\n')
        elif(b<9):
            print('你猜了{}次就猜中了'.format(b))
            print('还不错哦~\n')
        elif(b==9):
            print('继续加油哦~\n')
        b=0
        x=r.randint(1,99)
        print(x)