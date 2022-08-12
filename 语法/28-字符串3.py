 # 字符串的常用操作
# 字符串替换
s='hello,python'
print(s.replace('python','java'))
s1='hello,python,python,python'
print(s1.replace('python','java',2))
# 第一个参数为需要被替换对象，第二个为替换者，第三个为最大替换次数
lst=['hello','java','Python']
print('|'.join(lst))
print(''.join(lst))

t=('hello','Java','Python')
print(' '.join(t))
# join前面‘’里面符号为列表或元组元素的中间连接符
print('*'.join('Python'))

# 字符串的比较操作
print('apple'>'app') # True
print('apple'>'banana') # False
print(ord('a'),ord('b'))
# 字母相比较，比较ordinal value（原始值），先从第一个字母开始比
print(chr(97),chr(98))
# ord()和chr互为相反
print(ord('李'))
print(chr(26446))

'''
==与is的差别
==比较value
is比较id
'''
a=b='python'
c='python'
print(a==b) #True
print(a==c) #True
print(a is b) #True
print(a is c) #True

# 字符串的切片操作
'''字符串是不可变类型，不具备增删改操作，切片操作将产生新的对象'''
s='hello,Python'
s1=s[:5]
s2='!'
s3=s[6:]
print(s1+s2+s3)

print('-----------------切片[start:end:step]------------------')
print(s[1:5:1])
print(s[::2])
print(s[5:1:-1])