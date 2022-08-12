# -*- coding:utf-8 -*-
g=eval(input())
s=eval(input())
g.sort()
s.sort()
flag=0
flag_1=0
for i in g:
    for j in s:
        if(flag_1>=len(s)):
            break
        if(i>=s[flag_1]):
            flag+=1
            flag_1+=1
            break
print(flag)
