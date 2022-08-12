# -*- coding:utf-8 -*-
class Node:
    def __init__(self, data,_prev=None, _next=None):
        self.prev=_prev  # 指针域，指向前一个节点
        self.data = data   # 数据域
        self.next = _next  # 指针域，指向后一个节点

class Doublelinklist:
    def __init__(self):
        self.head= None  #链表的头节点
        self._length= 0 #链表的长度，链表的元素个数

    def is_empty(self):
        # 判断链表是否为空
        if self.head:
            return False
        else:
            return True

    def length(self):
        # 返回链表长度
        return self._length

    def nodes_list(self):
        # 返回链表中的所有节点的值组成的列表
        res=[]
        cur=self.head
        while cur:
            res.append(cur.data)
            cur=cur.next
        return res

    def add(self,data):
        # 往链表头部添加一个节点，值为data
        # 创建一个节点node
        node=Node(data)
        if self.is_empty():
            self.head=node
        else:
            # 让链表中原本的头节点的prev指向新建的节点
            self.head.prev = node
            # 先让node指向当前链表中的头节点
            node.next=self.head
            # 再让链表的head指向当前的node节点
            self.head=node
        # 添加节点后，链表的长度加一
        self._length+=1

    def append(self,data):
        # 往链表尾部添加节点，值为data
        # 新建一个节点，值为data
        node=Node(data)
        # 找到链表尾节点
        # 从头节点开始，遍历链表中的所有节点
        if self.head:
            cur=self.head
            while cur.next:# 每次判断当前节点的next是否为空,为空说明当前节点就是尾节点
                # 不为空则通过当前节点的next去访问下一个节点
                cur=cur.next
            # 让当前的尾节点的指针域指向node
            cur.next=node
            # 让node的prev指针域去指向原本的尾节点
            node.prev=cur
        else:
            self.head=node
        # 添加节点后，链表的长度加一
        self._length += 1

    def insert(self,pos,data):
        # 指定位置添加节点，值为data
        if pos<=0:
            self.add(data)
        elif pos>=self._length:
            self.append(data)
        else:
            # 新建一个节点node
            node=Node(data)
            cur=self.head
            # 找到链表索引为pos-1的节点
            for i in range(pos-1):
                cur=cur.next
            # 让node的next指向索引为pos的节点
            node.next=cur.next
            # 让索引为pos-1的节点的next指向node
            cur.next=node
            # 让索引为pos的节点指向新建的节点
            cur.next.prev=node
            # 让新建的node的prev指向上一个节点
            node.prev=cur
            # 链表的长度+1
            self._length += 1

    def remove(self,data):
        # 删除第一个值为data的节点
        cur=self.head
        while cur:
            if cur.data==data:
                # 如果前驱节点为空，说明要删第一个节点
                if cur==self.head:
                    self.head=cur.next
                else:
                    cur.prev.next=cur.next
                #  如果不是尾节点
                if cur.next:
                    cur.next.prev=cur.prev
                self._length -= 1
                return 0
            cur=cur.next
        return -1

    def modify(self,pos,data):
        # 修改指定位置的元素的值
        cur=self.head
        if 0<=pos<self._length:
            for i in range(pos):
                cur=cur.next
            cur.data=data
        else:
            print("您输入的值不符合范围")

    def search(self,data):
        # 查找节点是否存在
        cur=self.head
        while cur:
            if cur.data==data:
                return True
            cur=cur.next
        return False

if __name__ == '__main__':
    li=Doublelinklist() #新建一个链表类
    li.add(1)
    li.add(3)
    li.append(4)
    li.insert(0,2)
    li.remove(4)
    li.modify(2,2)
    print(li.head.data, li.length())
    print(li.nodes_list())
    print(li.is_empty())
    print(li.search(3))
