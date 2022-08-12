# -*- coding:utf-8 -*-
import re
emails="""
  asdsad@163.com
5465ds6asdds4a_dss6d4s5@163.com
sda_ds46@126.com
sad4564sfd@163.com
aaaa____@163.com
adsf479@163.com
"""
list=re.findall('(.*?)(\w)',emails)
for i in list:
    print(i)
print("\n")
# 一个()就是一个组
list=re.findall('(^[a-zA-Z][\w]{5,17}@(163|126)\.com$)',emails,re.MULTILINE)
for i in list:
    print(i[0])

# sub(pattern,repl,string,count=0,flags=0)
"""
pattern:    re.compile()方法生成pattern类型,也就是所有匹配的模式
repl:       可以是一段字符串或者一个方法
string:     需要被匹配和替换的原字符串
count:      指的是最大的可以被替换的匹配到的字符串的个数，默认是0，就是所有匹配到的字符串
flags:      标志位
"""
print("\n")
# 需求:匹配一个数字，把匹配结果的数字加1返回
def add(a):
    str_number=a.group()
    num=int(str_number)+1
    return str(num)

print(re.sub("\d+",add,"python=188"))

line="hello,world,beijing."
print(re.split('\W+',line))

print(re.split(":| ","info:lixinwei 20 hubei"))

line1="this is my tel:133-8888-5555"
# 非贪婪模式，需求：把电话和电话的描述信息尽可能分开，只能用正则表达式
result=re.match('(.+?)(\d+-\d+-\d+)',line1)
print(result.group(1))
print(result.group(2))
print(r"\n")