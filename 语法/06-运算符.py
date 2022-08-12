# 比较运算符
a,b=10,20
print('a大于b吗？',a>b) #Flase
print('a大于等于b吗？',a>=b) #Flase
print('a等于b吗？',a==b) # Flase 一个=为赋值运算符，两个==为比较运算符
print('a不等于b吗？',a!=b) # Ture
# =比较value，is比较id
a=10
b=10
print(a==b)  #Ture,ab值相同
print(a  is  b)  #Ture,ab标识相同
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2) #Ture
print(lst1  is  lst2) #Flase
print(id(lst1),id(lst2)) # id不相同
print(lst1  is not  lst2)  #Ture

# 布尔运算符
print('----------and----------')
a,b=1,2
print(a==1 and b==2) #and两边都为正确才是正确的
print('----------or----------')
# 只要有一个正确则是正确
print('----------not----------')
# 对bool类型运算数取反
print('----------in与not in----------')
s='hello world'
print('l' in s)
print('a' in s)
print('a' not in s)

# 位运算符
# &（让位于），二进制中同为1时结果为1，否则为0
print(4&8)
# |（让位或），同为0时结果为0
print(4|8)
# 左移位，高位溢出，低位补零，结果乘2，<<
# 右移位，低位溢出，高位补零，结果除以2,>>
print(4<<1) # 向左移一位
print(4<<2) # 向左移两位

# 运算符的优先级
'''
先算算术运算符，先乘除后加减，有幂运算先算幂运算
再算位运算符
然后算比较运算符
再进行布尔运算
最后是赋值运算符
有括号先算括号中的内容
'''

# 好
