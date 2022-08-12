# -*- coding:utf-8 -*-
# 先进先出

# 队列--顺序表实现
# 循环
class Queue:
    def __init__(self,size):
        # 以列表的最后一个元素作为队尾
        self.items=[None]*size  #先声明长度为size的数据区
        self.size=size  #队列的最大长度
        self.head=0  #队首的索引
        self._length=0 # 队列的长度

    def is_empty(self):
        return self._length==0

    def length(self):
        return self._length

    def push(self,item):
        if self.length()==self.size:
            raise ValueError("队列已满")
        # 先算出要添加元素的索引
        idx=(self.head+self.length())%self.size
        self.items[idx]=item
        self._length+=1

    def pop(self):
        # 抛出队首元素
        if self.is_empty():
            raise ValueError("队列是空的")
        value=self.items[self.head]
        self.head=(self.head+1)%self.size
        self._length-=1
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError("队列是空的")
        return self.items[self.head]

if __name__ == '__main__':
    queue=Queue(4)
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    # print(queue.peek())
    # print(queue.items)