#coding=gbk
# 链表是一种物理存储单元上非连续、非顺序的存储结构
# 数据元素的逻辑顺序通过链表中的指针链接次序实现
# 链表由一系列节点组成，节点可以在运行时动态生成
# 每个节点包括两个部分:储存数据元素的数据域、存储下一个节点地址的指针域
# 可以想存几个数据生成几个节点
"""
单向链表具备的操作:
is_empty()链表是否为空
length()链表长度
nodes_list()返回链表的所有结点的值组成的列表
add(data)链表头部添加节点，值为data
append(data)链表尾部添加节点，值为data
insert(pos,data)指定位置添加节点，值为data
remove(data)删除第一个值为data的节点
modify(pos,data)修改指定位置的元素的值
search(data)查找结点是否存在
"""


class Node:
    def __init__(self, data, _next=None):
        self.data = data   # 数据域
        self.next = _next  # 指针域


class SingleCyclelinklist:
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
        for i in range(self._length):
            res.append(cur.data)
            cur=cur.next
        return res

    def add(self,data):
        # 往链表头部添加一个节点，值为data
        # 创建一个节点node
        node=Node(data)
        if self.is_empty():  #判断是否为空
            self.head=node
            node.next=self.head
        else:
            # 先让node指向当前链表中的头节点
            node.next=self.head
            # 再让链表的尾节点指向Node
            cur=self.head
            while cur.next!=self.head:
                cur=cur.next
            cur.next = node
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
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = node  # 原本的尾节点指向新建的节点
        else:
            self.head=node
        node.next = self.head  # 新的尾节点指向当前的头节点
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
            # 链表的长度+1
            self._length += 1

    def remove(self,data):
        #判断链表是否为空，为空则没有值为data的节点
        if self.is_empty():
            return -1
        # 删除第一个值为data的节点
        cur=self.head
        flag=True #让第一次循环能进入
        prev=None #要删除的节点的前驱节点
        while cur!=self.head or flag:
            flag=False
            if cur.data==data:
                # 如果前驱节点为空，说明要删第一个节点
                if not prev:
                    # 找到尾节点
                    last_node=self.head
                    while last_node.next!=self.head:
                        last_node=last_node.next
                    # 让尾节点的next指向新的head
                    last_node.next=self.head.next
                    self.head=cur.next
                else:
                    prev.next=cur.next
                self._length -= 1
                return 0
            prev=cur
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
        if self.is_empty():
            return False
        cur=self.head
        flag=1
        while cur!=self.head or flag:
            flag=0
            if cur.data==data:
                return True
            cur=cur.next
        return False

if __name__ == '__main__':
    li=SingleCyclelinklist() #新建一个链表类
    print(li.head,li.length())
    li.add(1)
    li.add(3)
    li.append(4)
    li.insert(0,2)
    li.remove(2)
    li.modify(2,2)
    print(li.head.data, li.length())
    print(li.nodes_list())
    print(li.is_empty())
    print(li.search(3))