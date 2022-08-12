# -*- coding:utf-8 -*-
"""
查找:
在一组数据中找某一个特定项的算法过程
通常用来判断某个特定项是否在一组数据中，最终返回True或False
常用的查找算法:顺序查找,二分查找,树表查找,哈希查找等
"""
# 二分查找
# 要是有序列表
# O(logn)
"""
又称折半查找
要求待查表为有序表
将表中间的位置记录的关键字与查找关键字比较，如果相等则比较成功;
否则利用中间位置的记录缩小区间，继续查找缩小后的区间。
重复上面的步骤直到查找成功，或者子表不存在，则查找失败。
"""
def binary_search(nums,target,left,right):
    """
    :param nums: 待查找的数组，要求是升序的
    :param target: 要找的数字
    :param left: 区间的左边索引
    :param right: 区间的右边索引
    :return: target在nums中就放回True,否则放回False
    """
    # 递归的结束条件，left>right
    if left>right:
        return False
    # 找中间值
    mid=(left+right)//2
    # 判断中间值是否等于目标值
    if nums[mid]==target:
        return True
    # 如果中间值小于target,说明目标值只可能在中间值的右边区间
    if nums[mid]<target:
        # 左边区间往右缩
        return binary_search(nums,target,mid+1,right)
    # 如果中间值大于目标值，说明目标值只可能在中间值的右边区间
    return binary_search(nums, target,left ,mid-1)


test=[1 ,234,435,22563,2,324,345,45,34,23,52,234]
test.sort()
print(binary_search(test,234,0,len(test)-1) )
print(binary_search(test,5,0,len(test)-1))
