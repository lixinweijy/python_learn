def sky(a,b): # a，b称为形式参数，简称形参，位置在函数定义处
    c=a*b
    return(c)
# 定义sky里面的函数相乘c
print(sky(4,6)) # 4，6称为实际参数值，简称实参
# 这个a对应4，b对应6
def sky(a,b):
    c=a*(b-a)
    return(c)
print(sky(a=6,b=4)) # 左侧变量的名称称为  关键字参数，可以改变a，b对应的值

# 函数参数传递的内存分析
def key(a,b):
    a=100
    b.append(50)
    print(a,b)
    return

n1=11
n2=[22,33,44]
key(n1,n2)
print(n1,n2)
# n1未变  如果为不可变对象，函数值的修改不会影响实参的值
# 如果是可变对象，在函数体的修改会影响到实参值

# 函数的返回值
def zgg(num):
    odd=[] # 存奇数
    even=[] # 存偶数
    for i in num:
        if i%2==0:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst=[10,29,34,23,25,6,66,75]
print(zgg(lst))
'''
函数的返回值
（1）如果函数没有返回值【函数执行完毕之后，不需要给调用处提供数据】return可以不写
（2）函数返回值如果是一个，直接返回类型
（3）如果是多个，返回结果为元组
'''
def fun1():
    print('hello')
    # return

fun1()

def fun2():
    return'hello'

res=fun2()
print(res)

def fun3():
    return'hello','world'
print(fun3())
'''函数定义时，是否需要返回值，视情况而定'''

# 函数的参数定义
def fun(a,b=10): # b称为默认值参数
    print(a,b)

# 函数的调用
fun(100)
fun(20,30)

print('hello')
print('world')

print('hello',end='\t')
print('world')
