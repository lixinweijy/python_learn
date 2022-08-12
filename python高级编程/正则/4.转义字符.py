# -*- coding:utf-8 -*-
path="C:\\a\\b\\c"

import re

print(re.match("C:\\\\",path).group()) #两个斜线代表一个斜线 真好
# 字符串前面使用r，代表python中的原生字符串
print(re.match(r"C:\\",path).group())
