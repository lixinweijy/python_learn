# -*- coding:utf-8 -*-
# 快速排序
"""
分而治之
设定一个基准值pivot
将数组进行重新排列，所有比pivot小的放在其前面，比pivot大的放在其后面，这操作称为分区(partition)操作
对两边的数组重复前两个步骤
"""
# 快速排序的优化
"""
1.基准值的选取
(1)随机选取
(2)三数  mid

2.排序序列长度到一定大小后，改用插入排序

3.重复元素的选取
每次分割时，将与本次基准值相等的元素聚集在一起
(1)遇到相等的元素，放到区域的最左边或最右边
(2)分好区之后，相等的元素与基准值一边的元素进行交换

4.尾递归
"""


# 时间复杂度  O（nlogn）
# 列表法，耗费空间
# def quickSort(nums):
#     n=len(nums)
#     if n<=1:
#         return nums
#     pivot=nums[0]  #基准值
#     left=[]
#     right=[]
#     for i in range(1,n):
#         if nums[i]>pivot:
#             right.append(nums[i])
#         else:
#             left.append(nums[i])
#     return quickSort(left)+[pivot]+quickSort(right)

# 挖坑法
def partition(nums,left,right):
    pivot=nums[left]  #区域的第一个元素作为基准值
    while left<right:
        # 填坑
        while left<right and nums[right]>pivot:
            right -= 1
        nums[left]=nums[right]
        while left<right and nums[left]<=pivot:
            left+=1
        nums[right]=nums[left]
    nums[left]=pivot  #基准值的正确位置
    return left

def quickSort(nums,left,right):
    if left>=right:
        return
    # 分区 --> 分好区之后的基准值索引返回
    pivot_idx=partition(nums,left,right)
    # 左边的区域，left->pivot_idx-1
    quickSort(nums,left,pivot_idx-1)
    # 右边的区域，pivot_idx+1->right
    quickSort(nums,pivot_idx+1,right)
    # 分好的两边分别进行快速排序


test=[1 ,234,435,23543,2,324,345,45,34,23,52.34,234]
quickSort(test,0,len(test)-1)
print(test)
