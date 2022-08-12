 # 为什么将元组设置为不可变序列

'''不可变序列不能更改，操作对象不需要加锁，不容易出错'''
a=84,52
print(a)
t=(10,[20,30],9)
print(t)
print(type(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))
'''尝试将t[1]修改为100'''
'''不可修改元组，但是可以修改元组中可变序列的内容'''
print(id(100))
t[1].clear()
print(t)
t[1].append(100)
print(t)

# 元组的遍历
t=('Python','world',98)
'''第一种获取元组元素的方法，使用索引'''
print(t[0])
print(t[1])
print(t[2])
'''第二种方法，遍历元组'''
for item in t:
    print(item)