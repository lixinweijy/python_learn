# -*- coding:utf-8 -*-

# 桶排序
# 根据数组的最大值与最小值申请一些桶
# 将数组的元素放入桶中，并保证桶里是有序的
# 合并每个桶

def bucketSort(nums,size=5):
    # 根据数组的最大值与最小值确定要申请的桶的数量
    maxVal=max(nums)  #最大值
    minVal=min(nums)  #最小值
    bucketCount=(maxVal-minVal)//size +1  #桶的数量
    buckets=[[] for _ in range(bucketCount)]  #申请桶
    for num in nums:
        idx=(num-minVal) // size #num应该在哪个桶中，索引位index
        n =len(buckets[idx])  #求出当前桶中的元素个数
        i=0
        # print(n)
        # 找到第一个比num要大的元素
        while i<n and buckets[idx][i]<=num:
            i+=1
        buckets[idx].insert(i,num)
    print(buckets)
    # 合并桶
    nums.clear()
    for bucket in buckets:
        nums.extend(bucket)  #将每个桶中的元素放到nums中

test=[1 ,234,435,22563,2,324,345,45,34,23,52,234]
bucketSort(test)
print(test)

# 有小数在里面会报错，并且耗费空间大
# 稳定