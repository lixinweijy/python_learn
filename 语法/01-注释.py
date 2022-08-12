# 单行：hello world
print("hello world")

print("hello Python")  # 简单注释内容
"""
第一行注释
第二行注释
第三行注释
"""
'''
第一行注释
第二行注释
第三行注释
'''
# Ctrl+/也可以注释
# 将数据输出到文件中
a=open('D:/text.txt','a+')
print('hello world',file=a)
a.close()

print('hello','world','python')

# input  输入函数
present=input('大圣想要什么礼物呢？')
print(present,type(present))
# 从键盘输入两个整数，并求和
A=input('请输入一个加数')
A=int(A)
B=input('请输入另一个加数')
B=int(B)
print(type(A),type(B))
print(A+B)# 需要转换类型

c=int(input('请输入一个加数'))
d=int(input('请输入另一个加数'))
print(type(c),type(d))
print(c+d)

# 懂啦