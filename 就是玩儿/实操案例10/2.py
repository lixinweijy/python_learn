import random
def guess(num,guess_num):
    if num==guess_num:
        return 0
    elif num>guess_num:
        return 1
    else:
        return -1
num=random.randint(1,100)
try:
    for i in range(10):
        guess_num = int(input('我心里有个个1—100之间的数，请你猜一猜:'))
        result = guess(num, guess_num)
        if result == 0:
            print('猜对啦')
            break
        elif result == 1:
            print('猜小了')
        else:
            print('猜大了')
    else:
        print('sb,十次都猜不对')
except:
    print('输入格式错啦！')