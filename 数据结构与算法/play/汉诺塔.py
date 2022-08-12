# coding=gbk
import time
a=time.time()
i=1 #信号量，用来标记运动的步数
def tower(n,x,y): #定义函数表示移动方式
    global i  #声明全局变量，便于接受外界变量
    print(f"第{i}步，将{n}从{x}移到{y}上")
    i += 1  #运动一次i加1


def sport(n,a,b,c):
    if n == 1:  # 当n==1时终止回调
        tower(1, a, c)
    else:
        sport(n-1,a,c,b) # 首先，先将n-1个块从a上通过c弄到b上
        tower(n,a,c) #再将最后一个剩下的一个从a放在c上
        sport(n-1,b,a,c) #再将那n-1个从b上通过a弄到c

c=int(input("请输入盘子数:\n"))
sport(c,"A","B","C")
b=time.time()
print(f"需要{b-a}秒")
