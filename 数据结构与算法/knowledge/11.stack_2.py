# -*- coding:utf-8 -*-
# 栈 -- 用链表实现
class Node():
    def __init__(self,data,_next=None):
        self.data=data  #数据域
        self.next=_next  #指针域

class Stack:
    def __init__(self):
        self.__top=None  #栈顶元素
        self._size=0  #栈的元素个数

    def push(self,item):
        # 添加一个元素item到栈顶
        # 让self.top指向新的节点
        # 让新的节点的next指向原本的栈顶
        self.__top=Node(item,self.__top)
        self._size+=1

    def pop(self):
        # 判断栈是否为空
        if self.is_empty():
            raise ValueError("栈为空")
        value=self.__top.data
        self.__top=self.__top.next
        self._size-=1
        return value

    def top(self):
        # 判断栈是否为空
        if self.is_empty():
            raise ValueError("栈为空")
        return self.__top.data

    def is_empty(self):
        return self._size==0

    def size(self):
        return self._size

if __name__ == '__main__':
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.size())