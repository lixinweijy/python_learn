import random
price = random.randint(1000, 1500)
print('今日竞猜商品为小米扫地机器人:价格在[1000-1500]之间')
while True:
    a=int(input('您猜的价格为:'))
    if a>price:
        print('大了')
        continue
    elif a<price:
        print('小了')
        continue
    else:
        print('猜对了')
        break
print('商品的真实价格为:',price)