# -*- coding:utf-8 -*-
# 线性表:由零个或多个数据元素组成的有限序列，除了第一个节点外，均有唯一的前驱节点，除了最后一个节点外，均有唯一的后继节点
# 线性表主要是顺序存储结构或者链式存储结构

# 线性表：
"""
一般线性表:可以自由操作线性表
受限线性表:对线性表的操作受到限制
"""
# 栈
"""
只能对栈顶元素进行添加或者弹出
后进先出
"""

# 栈 -- 用顺序表来存
class Stack():
    def __init__(self):
        # 把列表最后一个元素作为栈顶
        self.__data=[]

    def push(self,item):
        # 添加一个元素item到栈顶
        self.__data.append(item)

    def pop(self):
        # 判断栈是否为空
        if self.is_empty():
            raise ValueError("栈为空")
        return self.__data.pop()

    def top(self):
        # 判断栈是否为空、
        if self.is_empty():
            raise ValueError("栈为空")
        return self.__data[-1]

    def is_empty(self):
        return self.__data==[]

    def size(self):
        return len(self.__data)

if __name__ == '__main__':
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.size())