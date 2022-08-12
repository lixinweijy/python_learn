import random as r

#生成一个100以内的随机数
a=r.randint(1,99)

#玩家输入数
b=eval(input("请猜一个100以内的整数:\n"))

print(a)
#判断
if b==a:
    print("猜对啦")
elif b>a:
    print("猜大了")
else:
    print("猜小啦")
