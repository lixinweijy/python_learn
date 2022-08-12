# -*- coding:utf-8 -*-
"""
|           匹配左右任何一个表达式
(ab)        将括号中字符作为一个分组
\number     匹配和前面索引为number的分组获取的内容一样的字符串
(?P<name>)  分组起别名
(?P=name)   引用别名为name的分组匹配到的字符串
"""
import re

# 需求1: 匹配从0到100的数字,包括100
print(re.match('[1-9]?\d$|100','98').group())

# 需求2：匹配网易邮箱，163.com和126.com都可以

emails="""
  asdsad@163.com
5465ds6asdds4a_dss6d4s5@163.com
sda_ds46@126.com
sad4564sfd@163.com
aaaa____@163.com
adsf479@163.com
"""
print(re.search('^[a-zA-Z][\w]{5,17}@(163|126)\.com$',emails,re.MULTILINE).group())

# 需求3:  匹配<h1>xxxxx<h1>

print(re.match('<[a-zA-Z]+\d*>\w*</[a-zA-Z]+\d*>','<h2>hello</h2>').group())

print(re.match(r'<([a-zA-Z]+\d*)>\w*</\1>','<h2>hello</h2>').group())

#第二种写法，匹配一个网页的嵌套标签
line='<div><p> hello </p></div>'
print(re.match(r'<(?P<n1>\w*)><(?P<n2>\w*)>.*</(?P=n2)></(?P=n1)>',line).group())
