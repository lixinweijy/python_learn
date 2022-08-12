# coding=gbk
# 1.map:把一个可迭代对象中的每个元素转换成一个新的对象，最后返回一个新的可迭代对象
list1=[1,2,3,4,5,6]
it1 = map(lambda x:x**2,list1)
print(list(it1))

# 2.reduce:把一个可迭代对象中每个元素做聚合处理，最后返回一个聚合的值
from functools import reduce

a=reduce(lambda x,y:x+y,list1)
print(a)

# 返回最大值
def getMax(x,y):
    if x>y:
        return x
    else:
        return y

print(reduce(getMax,list1))
# 3.filter是一个可迭代对象中的元素做过滤操作，如果func返回值为True则留下，否则过滤掉

emps=[
    {"name":"zhangshan","age":18,"salary":3000},
    {"name":"lisi","age":28,"salary":6000},
    {"name":"wangwu","age":38,"salary":9000}
]

# 需求，过滤留下大于18岁得到员工，返回一个迭代器
print(list(filter(lambda x:x["age"]>18,emps)))

# 4.max和min
# 需求，薪资最高
print(max(emps,key=lambda x:x["salary"]))
# 需求，薪资最低
print(min(emps,key=lambda x:x["salary"]))

# 5.sorted 把一个可迭代对象里面的每个元素排序，返回一个列表
print(sorted(emps,key=lambda x:x["age"],reverse=True))


