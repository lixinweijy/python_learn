# -*- coding:utf-8 -*-

# 排序算法的稳定性
# 稳定的算法会让原本有相等键值的记录维持相对次序
# 不稳定的算法可能会改变相等键值的记录的相对次序

# 冒泡排序

def bubbleSort(nums):
    n = len(nums) #得到数组长度
    for i in range(n-1):
        flag = False
        for idx in range(n-i-1):
            if nums[idx]>nums[idx+1]:
                nums[idx],nums[idx+1]=nums[idx+1],nums[idx]
                flag=True
        # 如果flag为False,说明本轮循环已经是有序的了,不需要再排序了
        if not flag:
            break

test=[1 ,234,435,23543,2,52.34,234]
bubbleSort(test)
print(test)
