# -*- coding:utf-8 -*-
a=input("")
print(~True)
print(~False)
if a.isalpha():
    a=chr(ord(a)+3)
    if  2+~a.isalpha():
        a=chr(ord(a)-26)
    print(a)
