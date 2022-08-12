# 整数类型  int
# 可以表示正数，负数，0
n1=50
n2=100
n3=150
print(n1,type(n1))
print(n2,type(n2))
print(n2,type(n3))
# 整数可以表示为二进制，十进制，八进制，十六进制
print('十进制',118)
print('二进制',0b10101111)
# 二进制0b开头
print('八进制',0o176)
# 八进制0o开头
print('十六进制',0x1EDC)
# 十六进制0x开头

# 浮点类型  float
# 浮点数不精确
a=3.1415926
print(a,type(a))
N1=1.1
N2=1.2
print(N1+N2)  # 不精确,并不是所有的都不准确
from decimal import Decimal
print(Decimal('1.1')+Decimal('1.2')) #Decimal 数字完全精确


# 布尔类型
# 只有true和false，true=1，false=0，可计算
f1=True
f2=False
print(f1+1)
print(f2+1)

# 字符串型  str
# 单引号和双引号都只能在同一行进行，三单和三双可分行进行
str1='人生苦短,我用python'
str2="人生苦短，我用python"
str3='''人生苦短，
我用python'''
str4="""人生苦短，
我用python"""
print(str1,type(str1))
print(str2,type(str2))
print(str3,type(str3))
print(str4,type(str4))


# 类型转换
name='小li'
age=18
print(type(name),type(age))  # 说明name与age类型不同
# 类型不同不能转换，需要转换类型
print('我叫'+name+'，今年'+str(age)+'岁') #将int类型通过str转化为str类型

print('----------str（）将其他类型转换为str类型----------')
a=100
b=10.0
c=True
print(type(a),type(b),type(c))
print(str(a),str(b),str(c))
print(type(str(a)),type(str(b)),type(str(c)))

print('----------int()将其他类型转换为整数类型----------')
a1='100'
a3=100.0
a4=True
print(type(a1),type(a3),type(a4))
print(int(a1),type(int(a1)),int(a3),type(int(a3)),int(a4),type(int(a4)))
# 将float类型转换为int类型时截取整数部分去掉小数
a5='hello'
a6='100.0'
print(type(a5),type(a6))
# print(type(int(a5)),type(int(a6))) # 报错，字符串必须为数字串（整数）

print('----------float将其他类型转换为浮点类型----------')
# 文字类无法转换为浮点类型；整数转换为浮点类型最后加.0
b1='100.0'
b2='10'
b3=True
b4='hello'
b5=1
print(type(b1),type(b2),type(b3),type(b4),type(b5))
print(float(b1),type(float(b1)))
print(float(b2),type(float(b2)))
print(float(b3),type(float(b3)))
# print(float(b4),type(float(b4)))  报错，非数字串
print(float(b5),type(float(b5)))

# ok

