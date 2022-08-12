# coding=gbk
def get_sum(*args):
    def tt():  # 定义函数
        s=0
        for n in args:
            s+=n
        return s
    return tt()  #返回函数
f1=get_sum(1,2,3,4,5,6)
print(f1)

print("______________________________________________")
# 需求: 得到所有小于100的所有质数
# 1、最小是2
# 2、除2外所有偶数都不是质数
# 3、思路:先得到所有大于1的奇数 ————》生成器,再把生成器中的所有元素过滤，去掉可以被小于元素本省的质数整除的

def odd_num(): #得到所有大于1的奇数的生成器
    n=1
    while True:
        n+=2
        yield n  #n为大于1的所有奇数

g1=odd_num()

def my_filter(n): # 判断是否能够整除的函数,n代表从生成器中拿到的一个质数
    return lambda  x:x%n>0 # x为一个奇数，n为小于当前x的一个质数

# 创建一个质数的生成器，最小的质数是2
def zhishu():
    yield 2
    g=odd_num() #得到所有大于1的奇数
    while True:
        x=next(g) #从生成器中拿到一个奇数
        g=filter(my_filter(x),g) # 过滤之后在赋值给g
        yield x

for n in zhishu():
    if n <100:
        print(n)
    else:
        break