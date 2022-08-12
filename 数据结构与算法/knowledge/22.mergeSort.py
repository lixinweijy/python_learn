# -*- coding:utf-8 -*-


# 归并排序
# 将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。

def merge(left,right):
    # 最终放回一个合并好的有序的数组
    # 比较left和right当前的第一个元素的大小
    # 定义两个变量,分别代表当前left与right的未添加进有序数组的第一个元素
    left_index,right_index=0,0
    res=[]  #有序数组
    while left_index<len(left) and right_index<len(right):
        if left[left_index]<right[right_index]:
            # 把左边数组里的元素添加的有序区中
            res.append(left[left_index])
            # 索引后移
            left_index+=1
        else:
            # 把右边数组里的元素添加到有序区中
            res.append(right[right_index])
            # 索引后移
            right_index+=1
    # 一方加完了，另一方还没有加完，需要加一下
    res+=right[right_index:]  #把剩余的未添加的元素全部添加到有序数组后面
    res+=left[left_index:]   #因为left,right本来就是一个有序数组，所以可以直接添加
    # 如果说left_index走完了，right还剩下一些元素，说明right里剩下的元素全部都比有序数组里的元素要大

    return res

def mergeSort(nums):
    # 分
    # 数组不能再分了
    if len(nums)<=1:
        return nums
    mid=len(nums)//2  #求出数组的中间位置
    left=mergeSort(nums[:mid])  #左边的数组
    right=mergeSort(nums[mid:])  #右边的数组
    # 合
    return merge(left,right)


test=[1 ,234,435,23543,2,324,345,45,34,23,52.34,234]
test=mergeSort(test)
print(test)
# 时间复杂度 O(nlogn)
# 稳定