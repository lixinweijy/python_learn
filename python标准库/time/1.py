# -*- coding:utf-8 -*-
import time
# 打印时间三种方式
"""
时间戳
结构化时间对象
格式化时间字符串
"""
# 时间戳:1970.1.1.0:00到指定时间的间隔，单位秒
print(time.time())

# 格式化时间对象
st=time.localtime()
print(type(st))
print(st)
# st本质上是一个元组，有9个元素
# 索引访问
print("今天是{}-{}-{}".format(st[0],st[1],st[2]))

print("今天是星期{}".format(st.tm_wday+1))
# 对象的属性只读

# 格式化时间字符串
print(time.ctime())

# strftime(时间格式)  "%Y-%m-%d %H:%M:%S"
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒"))

"""
%a 星期缩写
%A 星期
%b 月份缩写
%B 月份全称
%I 时 12小时制
%p pm还是am，一般与%I连用
%w 星期里第几天
%W 本周是今年第几周
"""

# sleep(miao)休息一会，参数单位为秒
# 三种格式之间的转换
# 时间戳 -> 结构化对象  gmtime()参数默认值为当前时间戳

# UTC 格林尼治时间
print(time.gmtime())
print(time.gmtime(time.time()))

# local
print("________________________________")
print(time.localtime())

# 结构化对象 -> 时间戳  mktime() 参数为结构化时间
print(time.time())
print(time.mktime(time.localtime()))

# 结构化对象 -> 格式化时间字符串
# strftime(format,st)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 格式化字符串 -> 格式化时间对象
# strptime(str,format)
strtime='2022-1-23 16:01:22'
print(time.strptime(strtime,"%Y-%m-%d %H:%M:%S"))