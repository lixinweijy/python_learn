'''可变序列  列表，字典(可使用增删改操作）'''
lst=[10,20,50]
print(id(lst))
lst.append(300)
print(id(lst))
'''不可变序列  字符串，元组（不可使用增删改操作）'''
s='hello'
print(id(s))
s=s+'world'
print(id(s))
print(s)

# 元组使用（）去定义，储存元素与列表相似
# 元组的创建方式
# 1.直接使用（）
t=('Python','world','98')
print(t)
print(type(t))

t2='Python','world',857 # 省略括号
print(t2)
print(type(t2))
t3=('Python')
print(t3)
print(type(t3)) # str类型，如果元组中只包括一个元素，需使用逗号和小括号
t4=('Python',)
print(t4)
print(type(t4))


# 2.使用内置函数tuple（）
t1=tuple(('Python','world',857))
print(t1)
print(type(t1))

'''空列表的创建方法'''
lst=[]
lst1=list()
'''空字典的创建方法'''
d={}
d1=dict()
'''空元组的创建方法'''
d2=()
d3=tuple()

print('空列表',lst,lst1)
print('空字典',d,d1)
print('空元组',d2,d3)