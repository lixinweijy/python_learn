# 列表元素的添加
lst=[10,20,'hello,''world']
for item in lst:
    print(item)
lst.append(100) # append--》在列表的后面添加一个元素
print(lst)# 并没有创建新的列表对象
lst2=['hello','world']
lst.extend(lst2) # extend-->在列表的后面最少添加一个元素
print(lst)
lst.insert(1,90) # insert-->在任意位置添加一个元素，前为在1位置添加90
print(lst)
lst3=[True,False,'hello']
# 在任意位置添加N多个元素
lst[1:]=lst3 #从1位置全部切掉，换为lst3
print(lst)

# 列表元素的删除
lst4=[10,20,30,40,50,60,30]
print(lst4)
lst4.remove(30)#从列表中移除一个元素，如果有重复元素则删除第一个
print(lst4)
lst4.pop(1)# 删除所在索引上的元素，如果没输入索引，则删除最后一个元素
print(lst4)

print('--------切片操作删除至少一个元素，将产生一个新的列表对象----------')
new_lst=lst4[1:3]
print(new_lst)
# 不产生新的列表对象，而是删除原列表中的内容
lst4[1:3]=[] # 用空列表将选中的原列表进行取代
print(lst4)

# clear=清除列表中的所有元素
lst4.clear()
print(lst4)

# del语句将列表对象删除
del lst4
# print(lst4)

# 列表的修改
list=[10,20,30,40]
# 一次只能修改一个值
list[2]=100
print(list)
list[1:3]=[300,400,500,600]
print(list)

# 列表元素的排序
list2=[20,50,90,40]
print('排序前的列表',list2)
# sort为升序  原函数调顺序
list2.sort()
print('排序后的列表',list2)
# 通过指定关键字参数，将列表中的元素进行降序排列
list2.sort(reverse=True)
print(list2)
list2.sort(reverse=False)
print(list2)

# 使用内置函数sorted()对列表进行，将产生一个新的列表对象
list5=[10,20,300,80,15]
print('原列表',list5)
new_list5=sorted(list5)
print(list5)
print(new_list5)
desc_list=sorted(list5,reverse=True)
print(desc_list)
# sort与sorted区别为sort是对原列表中的元素进行大小排序，sorted是产生一个新的列表进行排序，使用sorted原列表不发生改变

# 列表生成式
key=[i*i for i in range(1,10)]# 前面那个i*i为表达列表函数的表达式
print(key)

'''列表中的元素的值为2，4，6，8，10'''
key2=[ i*2 for i in range(1,6)]
print(key2)