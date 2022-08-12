'''[]定义列表，{}定义字典'''
# 以键值对的方式存储数据，无序序列，str，int为不可变序列，列表和字典为可变序列
scores={'张三':100,'李四':98,'王五':45}
# 创建字典：1.用{}；2.用内置函数dict
print(scores)
print(type(scores))
student=dict(name='jack',age=20)
print(student)
# 空字典
d={}
print(d)

# 字典元素的获取
# 第一种方式，使用[]
print(scores['张三'])

# 第二种方式，使用get（）方法
print(scores.get('张三'))

# 两种方法不同为如果查找的键不存在，[]会报错，get会输出None
print(scores.get('麻七',99)) # 99为麻七不存在时的默认值
