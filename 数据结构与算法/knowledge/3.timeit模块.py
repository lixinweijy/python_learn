# -*- coding: utf-8 -*-
# Timer(stmt,setup,timer,globals)
"""
stmt：statement，要测试的代码语句
setup:执行测试语句需要的环境，比如import语句
timer:定时器函数，有默认值，一般使用默认值即可
globals:代码的作用域，传一些要用到的变量组成的字典
"""
import timeit

# 向一个空列表中添加0~10000的元素


def fun_append():
    lst=[]
    for i in range(10001):
        lst.append(i)

def fun_insert_tail():
    lst = []
    for i in range(10001):
        lst.insert(-1,i)

def fun_insert_head():
    lst = []
    for i in range(10001):
        lst.insert(0,i)

def fun_extend():
    lst = []
    for i in range(10001):
        lst.extend([i])

def fun_plus_1():
    lst = []
    for i in range(10001):
        lst=lst+[i]

def fun_plus_2():
    lst = []
    for i in range(10001):
        lst+=[i]

def fun_comprehensions():
    lst = [i for i in range(10001)]

def fun_range():
    lst=list(range(10001))

fun_list=[fun_append,fun_insert_tail,fun_insert_head,fun_extend,
          fun_plus_1,fun_plus_2,fun_comprehensions,fun_range]
for i in fun_list:
    t=timeit.Timer('i',globals={'func':i})
    print(f"{i.__name__}运行时间:".ljust(30),t.timeit(1000),'秒')