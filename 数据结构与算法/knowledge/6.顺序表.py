#coding=gbk
"""
一体式顺序表：表头与元素地址相连
特点：更快
分离式顺序表: 表头与元素地址不相连，但是储存有元素地址
特点: 便于扩展
列表是元素外置的分离式顺序表
"""
import sys
lst=[]
init_allocated=sys.getsizeof(lst) #返回一个对象占用的内存，以字节为单位

for i in range(1,100):
    lst.append(i)
    now_allocated=sys.getsizeof(lst)-init_allocated
    print(f'当前元素的数量:{i},当前的占用内存:{now_allocated}  当前的容量是:{now_allocated//8}')