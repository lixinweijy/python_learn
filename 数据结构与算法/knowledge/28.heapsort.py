# -*- coding:utf-8 -*-
#堆是一种完全二叉树
#大根堆:每个结点的值都大于等于左右孩子结点
#小根堆:每个结点的值都小于等于左右孩子节点

"""
假设父节点的下标是p，那么对应左孩子小标就是2*p+1，对应右孩子的下标就是2*p+2
确定最后一个根节点的下标:
序列长度为n，最后一个就是n-1，就有n-1=2*p+1或者n-1=2*p+2
得出p=(n-2)/2  或者  p=(n-3)/2
"""

#heap:堆，堆大小，父节点的下标
def parent_down(heap,heap_size,parent_index):
    """实现父节点下沉"""
    left_child_index=2*parent_index+1  #左节点的下标
    while left_child_index<heap_size:
        #如果父节点有右孩子，那就比较两个孩子的大小，求出最大孩子的下标
        largest=left_child_index+1 if left_child_index+1<heap_size and heap[left_child_index+1]>heap[left_child_index] else left_child_index

        # 已知largest的值是最大孩子下标，这个值就可以和父节点的值进行比较了
        if heap[parent_index]>=heap[largest]:  #符节点大于等于任意一个子节点
            break
        # 否则父节点需要下沉(交换)
        heap[parent_index],heap[largest]=heap[largest],heap[parent_index]

        #第一次交换成功后，可能会影响原来节点的最大堆规则，所以继续重置父节点和子节点的下标，以便于进行第二次循环
        parent_index=largest
        left_child_index=2*parent_index+1

def heap_sort(my_list):
    """堆排序"""
    n=len(my_list)  #堆的长度(大小)

    #构建一个最大堆：从最后一个非叶子节点开始(从下往上开始)

    # start_index  表示：最后一个非叶子节点的下标
    end_parent_index=(n-2)//2
    for i in range(end_parent_index,-1,-1):
        parent_down(my_list,n,i)

    # 循环的从最大堆中删除根节点(堆顶)，把每次循环的最大值放在列表后面(升序排列)
    for i in range(n-1,0,-1):
        #把堆中第一个值(堆顶，最大值)交换到列表中的后面
        my_list[0],my_list[i]=my_list[i],my_list[0]
        #堆要开始进行调整
        parent_down(my_list,i,0)

if __name__ == '__main__':
    mylist=[1,3,2,5,6,7,8,3,3]
    heap_sort(mylist)
    print(mylist)

