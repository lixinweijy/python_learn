# coding=gbk
"""
青蛙跳台阶
n个台阶
1次可以跳1个台阶也可以跳2个台阶
青蛙要跳到第n个台阶，有多少种跳法
"""
stars = int(input("请问有几条台阶:\n"))
def fog(stars):
    if stars == 1:
        return 1
    elif stars == 2:
        return 2
    else:
        return fog(stars-1)+fog(stars-2)

print(f"有{fog(stars)}种方法")
