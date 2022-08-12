# -*- coding:utf-8 -*-

# 双端队列-链表实现

class Node:
    def __init__(self,data,_next=None):
        self.data=data  #数据域
        self.next=_next  #指针域

class Deque:
    def __init__(self):
        self.head=None #队首
        self.rear=None #队尾
        self._length=0 #队列的长度

    def is_empty(self):
        return self._length==0

    def length(self):
        return self._length

    def push(self,item):
        # 队尾添加一个元素item
        node=Node(item)
        # 队列为空
        if self.is_empty():
            self.head=node
            self.rear=node
        # 队列不为空
        else:
            self.rear.next=node
            self.rear=node
        self._length+=1

    def push_left(self,item):
        # 在队首添加一个元素
        node=Node(item)
        if self.is_empty():
            self.head=node
            self.rear=node
        else:
            node.next=self.head
            self.head = node
        self._length+=1

    def pop(self):
        # 弹出队首
        if self.is_empty():
            raise ValueError("双端队列为空")
        value=self.head.data
        self.head=self.head.next
        self._length-=1
        if self._length==0:
            self.rear=None
        return value

    def pop_right(self):
        # 弹出队首
        if self.is_empty():
            raise ValueError("双端队列为空")
        if self.length()==1:
            return self.pop()
        cur=self.head
        value=self.rear.data
        while cur.next!=self.rear:
            cur=cur.next
        self.rear=cur
        cur.next=None
        self._length-=1
        return value

    def peek(self):
        if self.is_empty():
            raise ValueError("双端队列为空")
        return self.head.data

    def items(self):
        cur=self.head
        while cur:
            print(cur.data,"->",end=" ")
            cur=cur.next
        print("")
if __name__ == '__main__':
    queue=Deque()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push_left(5)
    queue.items()
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())