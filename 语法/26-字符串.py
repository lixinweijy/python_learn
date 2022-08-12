# 字符串的驻留机制  不可变序列
# 驻留  开一个空间存储信息
# 可用sys强制驻留
a='Python'
b="Python"
c='''Python'''
print(a,id(a),b,id(b),c,id(c))
# 驻留机制（id相同）的几种情况
'''
1.字符串的长度为0或1时
2.符合标识符的字符串（字母，数字，下划线）
3.字符串只在编译时进行驻留，而非运行时
4.[-5,256]之间的数字
'''
s1='abc%'
s2='abc%'
print(s1 is s2)
# 字符串驻留机制的优缺点
'''直接利用，不用频繁创建和销毁字符串，提高效率，节约内存'''
# 字符串连接时建议使用join方法，而不是+，效率更高

# 字符串的查询操作
s='hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo')) # 最后一次出现的位置
print(s.rfind('lo')) # 最后一次出现的位置
# index查找不存在时抛异常，find不会而是返回-1

# 字符串的大小写转换操作的方法
'''
upper()字符全转化为大写字母
lower()全转化为小写字母
swapcase()大写转小写，小写转大写
capitalize()第一个字符转大写，其余小写
title()每个单词的第一个转为大写，其余小写
'''
a='hello,python'
b=a.upper()
print(a,id(a))
print(b,id(b))
# 转成大写后，会产生一个新的字符串对象
print(a.lower(),id(a.lower()))
# 全部是产生新的字符对象