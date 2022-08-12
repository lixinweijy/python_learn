# \n=换行
print('hello\nworld')
# \+转义功能首字母  n=newline
print('hello\tworld')
# 一个制表位四个单元格 \t=一个制表位  若前面占满制表位则重开一个，若没占满则补满当前制表位
print('hello\rworld')
# r=return \n=回车 world将hello进行了覆盖
print('hello\bworld')
# \b=退一格，将o退没了
print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'') #加入 \ 为了让单引号不出错
# 使转义字符不起作用原字符，r或者R
# 注意事项：最后‘一个’字符不能是反斜线
print(r'hello\nworld')


# 算数运算符
print(1+1) # 加法运算
print(1-1) # 减法运算
print(2*3) # 乘法运算
print(1/2) # 除法运算
print(1//2) # 整除运算，取小于该数的最大整数
print(11%2) # 取余运算
print(2**3) # 幂运算
print(9/-4)
print(-9//4) # 向下取最大整数
print(9%-4) # 取余运算时一正一负要遵循公式，余数=被除数-除数*商  9-（-4）*（-3）=-3
# 赋值运算符
print("----------支持参数赋值----------")
a=20
print(a)
a+=30
print(a)
a-=10
print(a)
a*=2 # type=int
print(a)
a/=3 # type=float
print(a)
a//=2
print(a)
a%=3
print(a)
print('----------解包赋值----------')
a,b,c=20,30,40
print(a,b,c)
print('----------交换两个变量的值----------')
a,b=10,20
print('交换之前：',a,b)
# 交换
a,b=b,a
print('交换之后：',a,b)

# 懂啦
