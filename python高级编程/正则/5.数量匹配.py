# -*- coding:utf-8 -*-

"""
*       匹配前一个字符出现0次或者无限次，即可有可无
+       至少出现一次
?       要么一次,要么没有
{m}     出现m次
{m,}    至少出现m次
{m,n}   出现从m到n次
"""

# 需求1:匹配第一个字母必须是大写，后面是小写或者没有
import re

print(re.match("[A-Z][a-z]*","MnasNNs").group())

# 需求2：匹配一个变量名
print(re.match(r"[A-Za-z_]+[\w]*","name1").group())
# print(re.match(r"[A-Za-z_]+[\w]*","4name1").group())

# 需求3：匹配0到99之间的任意一个数字
print(re.match('[0-9]?[0-9]',"2").group())
print(re.match('[1-9]?[0-9]',"22").group())

# 需求4：匹配密码(8-20位，可以是大小写的字母，数字，下划线)
print(re.match("[a-zA-Z0-9_]{8,20}","798465132").group())

# 练习5：匹配163的邮箱地址，用户名包含6~18个字符，可以是数字、字母、下划线，但是必须以字母开头
emails="""
asdsad@163.com
5465ds6asdds4a_dss6d4s5@163.com
sad4564sfd@163.com
sda_ds46@163.com
aaaa____@163.com
adsf479@163.com
"""
print(re.search('[a-zA-Z][\w]{5,17}@163\.com',emails).group())
