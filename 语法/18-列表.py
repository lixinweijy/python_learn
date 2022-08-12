lst=['hello','world',71] # lst储存了三个值
print(type(lst))
print(id(lst))
print(lst)

# 创建列表的第一种方式用[],中间用逗号隔开
# 第二种方式，使用内置函数list（）
lst2=list(['hello','world',85])
# 列表中值按顺序排列
# 正着从0开始，反着从-1开始
print(lst2[0],lst2[-3])

# 获取列表中指定元素的索引
lst=['hello','world',52,'hello']
# 如果列表中有相同元素，只返回列表中第一个元素的索引
print(lst.index('hello'))
# 如果查询元素列表中不存在，则会抛出ValueError
print(lst.index('hello',1,4)) #在索引为1到3的位置查找

lst3=['hello','world',98,'hello','world',123]
print(lst3[2])
print(lst3[-4])

'''获取列表中的多个元素
列表名[start:stop:step]
切片范围[start,stop)
'''
lst4=[10,20,30,40,50,60,70,80,90]
print(lst4[1:6:1])
# 切片出来的是新的对象
# start,step默认为1，stop默认到最后
# 步长为负数时第一个元素从最后一个开始
print(lst4[::-2])
print(lst4[7::-2])