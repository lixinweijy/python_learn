# -*- coding:utf-8 -*-

# 双端队列-顺序表实现

class Deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def length(self):
        return len(self.items)

    def push(self,item):
        self.items.append(item)

    def push_left(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def pop_right(self):
        return self.items.pop()

    def peek(self):
        return self.items[0]

if __name__ == '__main__':
    queue=Deque()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)
    queue.push_left(5)
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
    print(queue.pop())
