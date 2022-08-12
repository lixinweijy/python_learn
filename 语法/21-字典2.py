 # 判断元素是否存在于字典中
scores={'张三':100,'李四':98,'王五':45}
print('张三' in scores)
print('张三' not in scores)

# 字典元素的删除
del scores['张三'] # 删除指定的键值对
print(scores)
scores.clear() # 清空字典的元素
print(scores)
scores['陈六']=100 # 新增元素
print(scores)
scores['陈六']=50
print(scores) # 修改元素

# 获取字典的视图
'''
keys-->获取字典中所有key
values-->获取字典中所有value
items-->获取字典中所有的key，value对
'''
# 获取所有key
sky=scores.keys()
print(sky)
print(type(sky))
print(list(sky)) # 将所有的key组成的视图转化成列表
# 获取所有value
blue=scores.values()
print(blue)
print(type(blue))
print(list(blue)) # 将所有的value组成的视图转换成列表
# 获取所有item
zgg=scores.items()
print(zgg)
print(type(zgg))
print(list(zgg)) # 将所有的item组成的视图转化成列表，列表元素由元组组成

scores['张三']=40
print(scores)

for item in scores:
    print(item,scores[item],scores.get(item))

d={'name1':'张三','name':'李四'} # key不允许重复
print(d)
d={'name':'张三','nikename':'张三'}
print(d) # value可以重复
# 字典位置不能指定，由系统制定得来
# 字典中不能输入可变值,必须为不可变对象
'''
lst=[10,20,30]
d={lst:10}
print(d)
'''
# 字典生成式  for  in循环
items=['fruits','books','others']
prices=[92,42,62]
d={item:price  for item,price in zip(items,prices)}
print(d)# 两元素长短不一时以短的为主
