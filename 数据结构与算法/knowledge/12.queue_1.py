# -*- coding:utf-8 -*-
# 先进先出

# 队列--顺序表实现
class Queue:
    def __init__(self,size):
        self.size=size
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def length(self):
        return len(self.items)

    def push(self,item):
        if self.length()==self.size:
            raise ValueError("队列已满")
        # 最后一个元素作为队尾
        self.items.append(item)

    def pop(self):
        # 抛出队首元素
        if self.is_empty():
            raise ValueError("队列是空的")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise ValueError("队列是空的")
        return self.items[0]

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