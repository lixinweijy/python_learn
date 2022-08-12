# -*- coding:utf-8 -*-

# 队列 -- 链表实现

class Node:
    def __init__(self,data,_next=None):
        self.data=data  #数据域
        self.next=_next  #指针域

class Queue:
    def __init__(self):
        self.head=None  #对头
        self.rear=None  #队尾
        self._length=0  #长度

    def is_empty(self):
        return self._length==0

    def length(self):
        return self._length

    def push(self,item):
        # 最后一个元素作为队尾
        node=Node(item)
        # 如果队列是空
        if self.is_empty():
            self.head=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node
        self._length+=1

    def pop(self):
        # 抛出队首元素
        if self.is_empty():
            raise ValueError("队列是空的")
        value=self.head.data
        self.head=self.head.next
        self._length-=1
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError("队列是空的")
        return self.head.data

if __name__ == '__main__':
    queue=Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
