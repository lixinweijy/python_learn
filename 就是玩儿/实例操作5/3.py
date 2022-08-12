import random
b=random.randint(1,100)
for i in range(10):
    a = int(input('在我的心目中有一个数，请你猜一猜:'))
    if a > b:
        print('大了')
    elif a < b:
        print('小了')
    else:
        print('恭喜你猜对了')
        break
print(f'你一共猜了{i+1}次')
if i+1<3:
    print('真聪明')
elif i+1<=7:
    print('还凑活')
else:
    print('天哪，你真是个小傻逼')
