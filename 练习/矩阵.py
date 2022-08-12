# coding=gbk
def x():
    global x_lsts
    x_lsts=[]
    for i in range(n):
        x_lst=[]
        x_lsts.append(x_lst)
        for j in range(i,i+n):
            x_lst.append(j)
    return x_lsts
def y():
    global x_lsts
    x_lsts=[]
    for i in range(n):
        x_lst=[]
        x_lsts.append(x_lst)
        for j in range(i,i+n):
            x_lst.append(j)
    return x_lsts
def A():
    global x_lsts
    x_lsts=[]
    for i in range(n):
        x_lst=[]
        x_lsts.append(x_lst)
        for j in range(i,i+n):
            x_lst.append(j)
    return x_lsts
def B():
    global x_lsts
    x_lsts=[]
    for i in range(n):
        x_lst=[]
        x_lsts.append(x_lst)
        for j in range(i,i+n):
            x_lst.append(j)
    return x_lsts

def lun(n): # 游戏轮数
    num=1
    while n>1:
        num*=n
        n-=1
    print(num)
n=int(input("大小"))
m=int(input("取模"))
p=int(input("游戏轮数"))
def plus():
    while True:
        num1=0
        num2=0
        for i in range(n):
            for j in range(n):
                x[i][j]=A[i][j]*x[i][j]+B[i][j]*y[i][j]
                y[i][j]=A[i][j]*y[i][j]+B[i][j]*x[i][j]
                num1+=x[i][j]%m
                num2+=y[i][j]%m

# plus()