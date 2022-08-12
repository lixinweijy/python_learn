# -*- coding:utf-8 -*-
a=[1,2,34,5,76,4]
for i in a:
    if i==1:
        print('好')
        break
else:
    print("!")

for j in a:
    if j==9:
        print('好')
        break
else:
    print("!!")
# 所以只有正常退出，才会执行else