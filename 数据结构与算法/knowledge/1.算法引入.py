# coding=gbk
"""
如果a+b+c=1000,且a^2+b^2=c^2
求出a,b,b可能的组合
"""
# 第一步：分析需求
# 第二步：设计算法
# 第三步：代码实现

# 引入时间
import time

# 计算开始时间
A=time.time()

for a in range(10001):
    for b in range(10001):
        if a**2+b**2==(10000-a-b)**2:
            print(a,b,10000-a-b)

# 计算结束时间
B = time.time()

# 计算消耗时间
print(B-A)# 此时间不是确定的，小范围内变化

# 算法的特性
"""
输入项
输出项
有穷性
确切性
可行性
"""