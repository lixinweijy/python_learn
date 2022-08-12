# -*- coding:utf-8 -*-
import re

"""
.   匹配任意字符(不包括换行符)
[]  匹配字符集，区间中的集合，可匹配其中任意一个字符
\d  匹配数字，[0-9]
\D  非数字
\s  匹配空白字符，即空白、tab
\S  匹配非空字符
\w  单词字符(数字字母下划线)
\W  非单词字符
"""

one='a89'
print(re.match('.',one).group())

two='238'
print(re.match("\d{3}",two).group())  #匹配三个数字
print(re.match("[2,8]",two).group()) #2或者8
print(re.match("[2-8]",two).group()) #2到8

two_2="Hello Python"
print(re.match('[hH]',two_2).group())  #匹配大小写H

three="天空1号发射成功"
print(re.match('天空\d',three).group())