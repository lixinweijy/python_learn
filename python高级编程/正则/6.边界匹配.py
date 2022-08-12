# -*- coding:utf-8 -*-
import re
"""
^       匹配开始位置，多行模式下匹配每一行的开始(也有取反的意思，区分应用场景)
$       匹配字符串结尾
\b      匹配一个单词的边界
\B      匹配分单词的边界
"""

emails="""
  asdsad@163.com
5465ds6asdds4a_dss6d4s5@163.com
sad4564sfd@163.com
sda_ds46@163.com
aaaa____@163.com
adsf479@163.com
"""

#加一个^号放在[]外面，以什么开头，下面是以字母开头
print(re.search('^[a-zA-Z][\w]{5,17}@163\.com',emails,re.MULTILINE).group())  #MULTILINE看多行

#放在[]里面，取反
print(re.search('[^0-9]','1234'))

#$以什么结尾
print(re.search('^[a-zA-Z][\w]{5,17}@163\.com$',emails,re.MULTILINE).group())  #MULTILINE看多行

#\b 单词边界
print(re.search(r'.*\bChina\b','I Love China').group())

print(re.search(r'.*\bChina\b','I Love Chinana'))

#\B 不是单词边界
print(re.search(r'.*\BChina\B','I Love Chinana'))