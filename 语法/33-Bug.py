# 一包烟，一壶茶，一个bug调一天
# 常见的语法错误SyntaxError
'''
(1)
age=input('请输入你的年龄')
print(type(age))
if age>=18:
    print('成年人，你该付法律责任了')
'''
'''
(2)
while i<10:
   print(i)
'''
'''
1.漏了末尾冒号
2.缩进错误
3.中英文符号
4.字符串和数字拼在一起
5.没有定义变量
6.'=='比较运算符和赋值运算符混用
'''
# Bug的由来和分类
'''
一. 知识点不熟练
(1)索引越界问题IndexError
(2)append（）方法使用掌握不熟练
lst=[]
lst.append('A')
print('lst')
append一次只能输入一个元素
二. 思路解决方不清晰的法
(1)使用print找出错误
(2)使用注释注释掉错误的地方
三.被动掉坑
'''
# try...except...
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
    print('结果为：',result)
except ZeroDivisionError:
    print('对不起，除数不允许为0')
except ValueError:
    print('只能输入数字串')
print('程序结束')


# try...except...else
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为：',result)


# try...except...else...finally
try:
    a=int(input('请输入第一个整数'))
    b=int(input('请输入第二个整数'))
    result=a/b
except BaseException as e:
    print('出错了',e)
else:
    print('计算结果为：',result)
finally:
    print('谢谢您的使用')

'''
常见的异常类型
1.被0除--ZeroDivisionError
2.序列中没有此索引--IndexError
3.映射中没有这个键--KeyError
4.未声明/初始化对象（没有属性）--NameError
5.Python语法错误--SyntaxError
6.传入无效的参数--ValueError
'''
lst=[11,22,33,44]
# print(lst[4])  # IndexError  索引从0开始
dic={'name':'张三','age':20}
# print(dic['gender'])  #KeyError  无gender
# print(num) # NameError
# int(a)=20  # SyntaxError
# a=int('hello')  # ValueError

print('-----------traceback异常处理模块-------------')
# print(10/0)
import  traceback
try:
    print('-------------') # 横线到处跑
    print(1/0)
except:
    print(0)
'''
try:
    print('-----------')
    print(1/0)
except:
    traceback.print_exc() #打印异常
'''

i=1
while i < 10:
    print(i)
    i+=1
print(i)

# 练练练练练练