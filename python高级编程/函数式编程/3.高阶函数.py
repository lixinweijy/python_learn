# coding=gbk

# 定义一个函数，传入一个列表[1,2,3,4,5,6,7],返回一个新的列表 [每个数的阶层]

# 定义计算一个数字的阶层的函数
def test1(num):
    if num==1:
        return 1
    else:
        return num*test1(num-1)

# 定义计算一个数列的接触的函数
def test2(list,func):
    new_list=[]
    for i in list:
        new_list.append(func(i))
    return new_list

list1=[1,2,3,4,5,6,7]
print(test2(list1,test1))
