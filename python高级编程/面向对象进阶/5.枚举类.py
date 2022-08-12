# -*- coding:utf-8 -*-

#当项目中需要使用12个月份时
from enum import Enum

Month=Enum("抬头-month",("jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"))

# 把整个枚举中的所有值遍历出来

print(Month.__members__)# 枚举中的值自动从1开始，不会重复

#得到二月份值
print(Month["feb"].value)

#根据值2来得到月份的名字
print(Month(2).name)

#定义一个颜色的常量
class Color(Enum):  #第二种方式，自定义一个枚举类
    red=100
    green=200
    blue=300
    yellow=200
    #枚举中不允许key或value相同，如果value重复了，根据value取name只能拿到第一个

print(Color(200))