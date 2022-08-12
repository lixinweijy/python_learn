import random as r

#生成一个100以内的随机数
a=r.randint(1,99)
print(a)

b=eval(input("请猜一个100以内的整数:\n"))
flag=0
while(flag<9):
    #判断
    if b==a:
        print("猜对啦")
        break
    elif b>a:
        print("猜大了")
    else:
        print("猜小啦")
    
    #玩家输入数
    b=eval(input(""))
    flag+=1

if flag==9:
    print('太菜了')
