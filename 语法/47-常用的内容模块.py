import sys #提供与python解释器及其环境相关的标准库
print(sys.getsizeof(24)) #getsizeof方法判断函数字节
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time #提供与时间相关的各种函数的标准库
print(time.time())
print(time.localtime(time.time()))

import urllib.request
print(urllib.request.urlopen('http://www.baidu.com').read())

'''
sys 提供与python解释器及其环境相关的标准库
time 提供与时间相关的各种函数的标准库
os  提供了访问操作系统服务功能的标准库
calendar 提供与日期相关的各种函数的标准库
urllib 用于读取来自网上（服务器）的数据标准库
json 用于使用JSON序列化和反序列化对象
re 用于在字符串中执行正则表达式匹配和替换
math 提供标准算术运算函数的标准库
decimal 用于进行精确控制运算精度、有效数位和四舍五入操作的十进制运算
logging 提供了灵活的记录事件、错误、警告和调试信息等
'''
