# -*- coding:utf-8 -*-
import os
import re
# 遍历指定目录下的所有文件(包括子文件下的文件)
# print(os.walk('./'))
for dirpath,dirnames,files in os.walk("../"):
    print("发现文件夹",dirpath)
    print(dirnames)  #dirpath这个文件夹下的子文件列表
    print(files)
print("\n\n")

#startswith()  endswith()
#找到所有py文件
lst=os.listdir()
# print(lst)
for i in lst:
    if i.endswith(".py"):
        print(i)
print()
# 以1开头
for i in lst:
    if i.startswith("1"):
        print(i)

# glob模块
import glob
# *代表0个或多个字符  ?代表1个字符   [1-5]1到5  !非  像正则表达式

print(glob.glob("1*.py"))

print(glob.glob('**/*.py',recursive=True))  #**表示任意层文件，recursive表示递归

# fnmatch模块
import fnmatch
print(fnmatch.fnmatch("1.作.py","2*.py"))  #验证文件名是否符合这个规则
