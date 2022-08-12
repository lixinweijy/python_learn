#coding=gbk
# ������һ������洢��Ԫ�Ϸ���������˳��Ĵ洢�ṹ
# ����Ԫ�ص��߼�˳��ͨ�������е�ָ�����Ӵ���ʵ��
# ������һϵ�нڵ���ɣ��ڵ����������ʱ��̬����
# ÿ���ڵ������������:��������Ԫ�ص������򡢴洢��һ���ڵ��ַ��ָ����
# ������漸���������ɼ����ڵ�
"""
��������߱��Ĳ���:
is_empty()�����Ƿ�Ϊ��
length()������
nodes_list()������������н���ֵ��ɵ��б�
add(data)����ͷ����ӽڵ㣬ֵΪdata
append(data)����β����ӽڵ㣬ֵΪdata
insert(pos,data)ָ��λ����ӽڵ㣬ֵΪdata
remove(data)ɾ����һ��ֵΪdata�Ľڵ�
modify(pos,data)�޸�ָ��λ�õ�Ԫ�ص�ֵ
search(data)���ҽ���Ƿ����
"""


class Node:
    def __init__(self, data, _next=None):
        self.data = data   # ������
        self.next = _next  # ָ����


class Singlelinklist:
    def __init__(self):
        self.head= None  #�����ͷ�ڵ�
        self._length= 0 #����ĳ��ȣ������Ԫ�ظ���

    def is_empty(self):
        # �ж������Ƿ�Ϊ��
        if self.head:
            return False
        else:
            return True

    def length(self):
        # ����������
        return self._length

    def nodes_list(self):
        # ���������е����нڵ��ֵ��ɵ��б�
        res=[]
        cur=self.head
        while cur:
            res.append(cur.data)
            cur=cur.next
        return res

    def add(self,data):
        # ������ͷ�����һ���ڵ㣬ֵΪdata
        # ����һ���ڵ�node
        node=Node(data)
        # ����nodeָ��ǰ�����е�ͷ�ڵ�
        node.next=self.head
        # ���������headָ��ǰ��node�ڵ�
        self.head=node
        # ��ӽڵ������ĳ��ȼ�һ
        self._length+=1

    def append(self,data):
        # ������β����ӽڵ㣬ֵΪdata
        # �½�һ���ڵ㣬ֵΪdata
        node=Node(data)
        # �ҵ�����β�ڵ�
        # ��ͷ�ڵ㿪ʼ�����������е����нڵ�
        if self.head:
            cur=self.head
            while cur.next:# ÿ���жϵ�ǰ�ڵ��next�Ƿ�Ϊ��,Ϊ��˵����ǰ�ڵ����β�ڵ�
                # ��Ϊ����ͨ����ǰ�ڵ��nextȥ������һ���ڵ�
                cur=cur.next
            # �õ�ǰ��β�ڵ��ָ����ָ��node
            cur.next=node
        else:
            self.head=node
        # ��ӽڵ������ĳ��ȼ�һ
        self._length += 1

    def insert(self,pos,data):
        # ָ��λ����ӽڵ㣬ֵΪdata
        if pos<=0:
            self.add(data)
        elif pos>=self._length:
            self.append(data)
        else:
            # �½�һ���ڵ�node
            node=Node(data)
            cur=self.head
            # �ҵ���������Ϊpos-1�Ľڵ�
            for i in range(pos-1):
                cur=cur.next
            # ��node��nextָ������Ϊpos�Ľڵ�
            node.next=cur.next
            # ������Ϊpos-1�Ľڵ��nextָ��node
            cur.next=node
            # ����ĳ���+1
            self._length += 1

    def remove(self,data):
        # ɾ����һ��ֵΪdata�Ľڵ�
        cur=self.head
        prev=None #Ҫɾ���Ľڵ��ǰ���ڵ�
        while cur:
            if cur.data==data:
                # ���ǰ���ڵ�Ϊ�գ�˵��Ҫɾ��һ���ڵ�
                if not prev:
                    self.head=cur.next
                else:
                    prev.next=cur.next
                self._length -= 1
                return 0
            prev=cur
            cur=cur.next
        return -1

    def modify(self,pos,data):
        # �޸�ָ��λ�õ�Ԫ�ص�ֵ
        cur=self.head
        if 0<=pos<self._length:
            for i in range(pos):
                cur=cur.next
            cur.data=data
        else:
            print("�������ֵ�����Ϸ�Χ")

    def search(self,data):
        # ���ҽڵ��Ƿ����
        cur=self.head
        while cur:
            if cur.data==data:
                return True
            cur=cur.next
        return False

if __name__ == '__main__':
    li=Singlelinklist() #�½�һ��������
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

"""
    ����    ����    ˳���
  ����Ԫ��   O(n)    O(1)
ͷ������/ɾ�� O(1)    O(n)
β������/ɾ�� O(n)    O(1)
�м����/ɾ�� O(n)    O(n)
"""
