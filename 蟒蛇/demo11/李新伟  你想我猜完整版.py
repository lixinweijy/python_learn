import random as r

#生成一个100以内的随机数
a=r.randint(1,99)
print("随机数为:{}".format(a))
flag=0
def improve():
   try:
        z=0
        while z!="n":
            global flag
            while flag<9:
                #玩家输入数
                global a
                flag+=1
                if flag==1:
                    b=eval(input("请猜一个100以内的整数:\n"))
                else:
                    b=eval(input(""))
                #判断范围
                if b>99 or b<1:
                    print("数据输入错误，要在规定范围内输入")
                    flag-=1
                    continue
                #判断大小
                if b==a:
                    print("猜对啦,共用了{}次".format(flag))
                    break
                elif b>a:
                    print("猜大了")
                else:
                    print("猜小啦")
            #判断水平
            if flag<6:
                print('王者段位')
            elif flag<8:
                print("钻石段位")
            else:
                print("青铜段位")
            z=input("是否再来一局(输入n退出)\n\n")
            if z!="n":
                a=r.randint(1,99)
                print("随机数为:{}".format(a))
                flag=0
   except:
        print("输入有误，再来一次吧")
        flag-=1
        improve()
improve()
print("游戏结束")