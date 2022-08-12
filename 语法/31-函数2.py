 #函数的参数定义
def fun(*sky): #不知道有几个参数时用*,只能定义一个，位置形参
    print(sky)
    print(sky[0])


'''
def fun(*sky,*key):
    pass
    以上代码程序会报错，可变的位置参数只能是一个
'''
fun(10)
fun(10,10)
fun(10,20,30)

def fun(**sky):# 两个**变为字典,称为关键字参数
    print(sky)

fun(a=10)
fun(a=10,c=20,b=30)
print('hello','world','java')

'''
def fun(**sky,**key):
    pass
以上代码报错，个数可变的关键字参数只能是一个
'''
def fun(*sky,**key):
    pass

'''
def fun(**sky,*key):
    pass
报错，在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求个数可变的位置形参在关键字形参之前
'''

def fun(a,b,c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
# 函数的调用
fun(10, 20, 30) # 函数调用时的位置传参
lst=[11,22,33]
fun(*lst) # 在函数调用时，将每个元素对转化为位置实参传入
fun(a=100,c=300,b=200) # 关键字实参
dic={'a':111,'b':222,'c':333}
fun(**dic)

def fun1(a,b=10):
    print('a=',a)
    print('b=',b)

def fun2(*sky): # 个数可变的位置形参
    print(sky)

def fun3(**key): # 个数可变的关键字形参
    print(key)

fun1(10,20)
fun2(10)
fun2(10,20,30,40)
fun3(a=10,b=20,c=30,d=40)

print('-------------------------------')
def fun4(a,b,*,c,d):  #从*之后的参数，在函数调用时只能采用关键字参数传递
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)

# 调用fun4函数
# fun4(10,20,30,40) # 位置实参传递
fun4(d=10,b=20,c=30,a=40) # 关键字实参传递
fun4(1,2,c=6,d=8) # 前两个位置实参传递，后两个关键字实参传递
'''需求， c，d只能采用实参传递'''
# 在c前面加个*可完成需求

'''函数定义时形参的顺序问题'''
def fun5(a,b,*,c,d,**sky):
    pass
def fun6(*sky,**key):
    pass
def fun7(a,b=10,*sky,**key):
    pass

# 变量的作用域
# 局部变量
def fun(a,b):
    c=a+b # c为局部变量，因为c在是函数体内进行定义的变量，a，b为函数的形参，作用服务是函数内部，相当于局部变量
    return c
# print(a) 报错，因为ac超出了作用域
# print(c)
name='杨老师' # name在函数内部外部都可以使用————》称为全局变量
def fun2():
    print(name)
fun2()

def fun3():
    global age # 局部变量使用global声明，这个函数实际上就变成全局变量了
    age=20
    print(20)
fun3()
print(age)