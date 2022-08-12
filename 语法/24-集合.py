# 集合的概述
'''
内置数据结构
可变类型
没有value的字典
'''
# 第一种创建方式，直接创建
s={2,3,4,5,6,7,7}
print(s)
# 集合中的元素不允许重复
# 第二种创建方式使用set()
s1=set(range(6))
print(s1,type(s1))

s2=set([1,2,3,4,5,6,6])
print(s2,type(s2))

s3=set([1,2,3,4,5,96]) # 集合中的元素是无序的
print(s3,type(s3))

s4=set('Python')
print(s4,type(s4))

s5=set({12,3,5,66,89})
print(s5,type(s5))

# 定义一个空集合
s6={} # dict字典类型
print(type(s6))

s7=set()
print(type(s7))

# 集合的相关操作
'''集合元素的判断操作'''
a={10,20,30,40,50,60,405,70}
print(10 in a) # True
print(100 in a) # False
print(10 not in a) # False
print(100 not in a) # True

'''集合元素的新增操作'''
a.add(80) # add 一次添加一个元素
print(a)
a.update({100,200,300}) # update 一次至少添加一个元素
print(a)
a.update([12,45])
print(a)
a.update((34,52,62))
print(a)

'''集合元素的删除操作'''
a.remove(100) # 一次删除一个指定元素，如果该元素不存在则抛出KeyError
print(a)
# a.remove(500) KeyError:500
print(a)
a.discard(500) # 一次删除一个指定元素，如果该元素不存在不抛异常
a.pop() # 任意删除元素，不能指定参数，指定参数则抛异常
print(a)
a.clear() # 清空集合中的元素
print(a)