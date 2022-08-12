# -*- coding:utf-8 -*-

# 希尔排序
# 插入排序的优化版本
"""
设定一个增量gap，将数组按照gap分组
对每一组进行插入排序
缩小增量gap,重复前两个步骤，直到gap缩小到1，那么最后一次排序就是插入排序
"""
# 以下两种方法皆可

# def shellSort(nums):
#     n=len(nums)  #列表长度
#     # 设定一个增量gap
#     gap=n//2
#     while gap>=1:
#         # 分组
#         for i in range(gap):
#             # 对每一个小组进行插入排序
#             for j in range(i,n-gap,gap):
#                 curNum=nums[j+gap]  #无序区的第一个元素的值
#                 idx=j #有序区的最后一个元素的索引
#                 while idx>=0 and nums[idx]>curNum:
#                     nums[idx+gap]=nums[idx] # 把小组的有序区的元素往后挪
#                     idx -=gap #指针往前移，以此来从后往前遍历小组的有序区
#                 nums[idx+gap]=curNum
#         gap//=2  #缩小增量

#复杂度由gap值决定
# 算法第四版中，罗伯特总结出一种好的设置方法
# 如下:
# O(nlogn)

def shellSort(nums):
    n=len(nums)  #列表长度
    # 设定一个增量gap
    gap=1
    while gap<n//3:
        gap=gap*3+1
    while gap>=1:
        # 分组
        for i in range(gap,n):
            curNum=nums[i]  #当前要插入的无序区的元素的值
            idx=i-gap  #当前元素所在小组的有序区的最后一个元素的索引
            while idx>=0 and nums[idx]>curNum:
                nums[idx+gap]=nums[idx]
                idx-=gap
            nums[idx+gap]=curNum
        gap//=3  #缩小增量

test=[1 ,234,435,23543,2,324,345,45,34,23,52.34,234]
shellSort(test)
print(test)

# 不稳定，较快