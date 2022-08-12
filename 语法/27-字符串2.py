# 字符串内容对齐的操作
'''
center()居中对齐
ljust（）左对齐
rjust（）右对齐
zfill（）右对齐
'''
s='hello,python'
print(s.center(20,'*'))
print(s.ljust(20,'*'))
# 设置的宽度小于字符串则输出原字符串
# 不写填充符则用空格代替
print(s.ljust(20))
print(s.rjust(20,'*'))
print(s.zfill(20))
print('-8910'.zfill(8))

# 字符串的劈分操作 从左开始劈分split
s='hello world Python'
a=s.split()
print(a)
# 默认将空格定为劈分字符串，可用sep自定义劈分字符串
b='hello|world|python'
c=b.split(sep='|')
print(c)
d=b.split(sep='|',maxsplit=1)
print(d)
# maxsplit后对应数字为最大劈分次数
# rsplit从右开始劈分
print(s.rsplit())
print(b.rsplit(sep='|',maxsplit=1))

# 判断字符串的方法
'''
isidentifier()判断字符串是不是合法的标识符
isspace()判断是否全部由空白字符组成（回车，换行，水平制表符）
isalpha()是否全部由字母组成
isdecimal()是否全部由十进制数字组成
isnumeric()是否全部由数字组成
isdigit()是否只包含数字
isalnum()是否全部由数字和字母组成
'''
s='hello,python'
print('1.',s.isidentifier()) #False
print('2.','hello'.isidentifier()) #True
print('3.','\t'.isspace()) #  True