 # 格式化字符串
'''
(1)
%做占位符
%s 字符串
%i,%d 整数
%f浮点数
'''
name='张三'
age=20
print('我叫%s,今年%d岁'%(name,age))
'''
(2)
{}做占位符
'''
print('我叫{0},今年{1}岁'.format(name,age))
'''
(3)
f-string
'''
print(f'我叫{name}，今年{age}岁')

print('%10d'%99) # d前面的10表示宽度
print('%.3f'%3.1415926) # f前面的.3表示保留三位小数
# 同时表示宽度精度
print('%10.3f'%3.1415926) # 总宽度为10，精度为小数点后3位
print('hellohello')
print('{0:.3}'.format(3.1415926)) # .3表示一共是3位数
print('{:.3f}'.format(3.1415926)) # .3f表示3位小数
print('{0:10.3f}'.format(3.1415926)) # 表示宽度为10，精度为小数点后3位

# 字符串的编码与解码
# 字符串的编码转换

s='天涯共此时'
# 编码
print(s.encode(encoding='GBK')) # 在GBK这种编码格中一个中文占两个字节
print(s.encode(encoding='UTF-8')) # 在UTF-8这种编码格中，一个中文占三个字节

# 解码
# byte代表的是一个二进制数据
byte=s.encode(encoding='GBK')
print(byte.decode(encoding='GBK'))
# 不能用GBK编码，UTF-8解码，不能用一种方法编码，另一种方法解码
