# -*- coding:utf-8 -*-

# 选择排序

def selectionSort(nums):
    n=len(nums)  #数组的长度
    for i in range(n-1):
        # 找到无序区中最小的元素
        min_idx=i #无序区中最小的元素的索引
        for j in range(i+1,n):
            if nums[j]<nums[min_idx]:
                min_idx=j
        # 执行完上面的循环后
        # min_idx就是无序区中最小的元素的索引
        # 把最小元素和有序区的最后一个元素交换位置
        nums[i],nums[min_idx]=nums[min_idx],nums[i]

test=[1 ,234,435,23543,2,52.34,234]
selectionSort(test)
print(test)

# 选择排序是不稳定的
