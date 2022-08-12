 # 集合间的相关关系
#  集合是否相等用==或！=进行判断
# 元素相同集合相等
s={10,20,30,40}
s1={40,20,30,10}
print(s==s1) # True
print(s!=s1) # False
# 无序性

'''一个集合是否是另一个集合的子集'''
# issubset是子集
a1={10,20,30,40,50,60}
a2={10,20,30,40,70}
a3={10,20,90}
print(a2.issubset(a1)) # True
print(a3.issubset(a1)) # False

'''一个集合是否是另一个集合的超集'''
# issuperset是超集
print(a1.issuperset(a2)) # True
print(a1.issuperset(a3)) # False

'''两个集合是否含有交集'''
# isdisjoint没有交集
print(a2.isdisjoint(a3)) # False有交集
a4={100,200,300}
print(a2.isdisjoint(a4)) # True没有交集
print("______________________________")
# 集合的数学操作
# （1）交集
print(a2.intersection(a1))
print(a1 & a2)  #intersection() 与 & 等价
print(a1)
print(a2)
# （2）并集
print(a1.union(a2))
print(a1|a2) # union与|等价
print(a1)
print(a2)
# （3）差集
print(a1.difference(a2))
print(a1-a2) # difference与-等价
print(a1)
print(a2)
# (4) 对称差集  =非交集
print(a1.symmetric_difference(a3))
print(a1^a3) # symmetric_difference与^等价

# 列表生成式
lst=[i*i for i in range(10)]
print(lst)
# 集合生成式 (讲列表生成式的[]改为{}）
s={i*i for i in range(10)}
print(s)


'''
列表(list)   可变   可重复  有序  []
元组（tuple） 不可变 可重复  有序  （）
字典（dict）  可变   key不可重复，value可重复  无序  {key：value}
集合(set)    可变   不可重复 无序  {}
'''