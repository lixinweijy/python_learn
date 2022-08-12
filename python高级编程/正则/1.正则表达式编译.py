# -*- coding:utf-8 -*-
import re

tel_1="""4665123asdads12323658451580721633013797334335dsaasadssad4a545as21sad"""

tel_2="15837846338ccc"


pattern=re.compile(r'1[3,9]\d{9}') #编译正则表达式，得到一个编译对象
result=pattern.search(tel_1)  #search  只会返回第一个匹配的结果  如果没有匹配成功，则返回None
print(result)
print(result.group(0))  #返回匹配的结果
print(result.span(0))  #返回第一个匹配的结果的下标

# result1=pattern.match(tel_2)  #match函数是从第一个字符开始匹配，如果第一个字符不符合条件，就返回None
# print(result1.group(0))

