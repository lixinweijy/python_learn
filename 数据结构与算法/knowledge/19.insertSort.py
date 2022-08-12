# -*- coding:utf-8 -*-

# 插入排序

def insertSort(nums):
    n=len(nums)  #列表长度
    for i in range(n-1):
        curNum=nums[i+1]  #无序区第一个元素的值
        idx = i  #有序区的最后一个元素的索引
        while nums[idx]>curNum and idx>=0:
            nums[idx+1]=nums[idx]  #把有序区的元素往后挪一位
            idx-=1  #索引往前移,以此来从后往前遍历有序区
        nums[idx+1]=curNum

test=[1 ,234,435,23543,2,52.34,234]
insertSort(test)
print(test)

# 稳定
