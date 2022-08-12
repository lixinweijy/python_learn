# -*- coding:utf-8 -*-
import heapq
class MedianHolder():
    """
    采用大项堆和小项堆来求中位数
    """
    def __init__(self,lst):
        # lst初始的数组(乱序)
        # 把整个lst中的数据存放到两个堆中
        self.first_array=lst #小项堆中的数据存放到first_array中
        self.second_array=[]  #大项堆中数据存放到second_arrry
        #大项堆中数据总数 是 n/2 ,或者n/2+1（n为奇数）
        #小项堆中数据总数 是 n/2
        n=len(lst)  # 总的数据条数
        heapq.heapify(self.first_array)  #小项堆结构
        #把小项堆中的数据移到大项堆中

        move_size=n/2 if n%2==0 else (n//2)+1
        for i in range(move_size):
            self.second_array.append(-heapq.heappop(self.first_array))
        heapq.heapify(self.second_array)
        # print(self.second_array)

    def add(self,num):
        """动态添加新的数字，造成中位数改动"""
        #如果新插入的数据大于等于小项堆的堆顶位置，则插入到小项堆，否则插入到大项堆
        if num>=self.first_array[0]:
            heapq.heappush(self.first_array,num)
            # 如果大项堆中数据个数小于小项堆数据个数，则需将小项堆堆顶数据移到大项堆
            if len(self.second_array)<len(self.first_array):
                heapq.heappush(self.second_array,-heapq.heappop(self.first_array))
        else: # 新插入的数据，插入到大项堆
            heapq.heappush(self.second_array,-num)
            if len(self.second_array)>len(self.first_array)+1:
                heapq.heappush(self.first_array, -heapq.heappop(self.second_array))

    def get_median(self):
        """返回中位数"""
        return -self.second_array[0]

if __name__ == '__main__':
    a=MedianHolder([2,6,4,8,5])
    print("中位数是:{}".format(a.get_median()))
    a.add(3)
    print("中位数是:{}".format(a.get_median()))