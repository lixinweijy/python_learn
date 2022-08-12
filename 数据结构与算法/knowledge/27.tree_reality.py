# -*- coding:utf-8 -*-
# 深度遍历
# 先序遍历:
# 遍历顺序:
# 根节点-->左子树-->右子树

# 中序遍历:
# 遍历顺序:
# 左子树-->根节点-->右子树

# 后序遍历:
# 遍历顺序:
# 左子树-->右子树-->根节点

class Node:
    def __init__(self,val):
        self.val=val  #数据域
        self.left=None  #左指针域
        self.right=None   #右指针域

class Tree:
    def __init__(self):
        self.root=None  #树的根节点

    def add(self,val):
        # 层次遍历，广度优先遍历
        # val 要添加的节点的值
        # 往树中添加一个节点，并保证添加之后这棵树依旧是一颗完全二叉树
        node=Node(val)
        # 判断树是否为空，如果为空，直接将node设置为根节点
        if not self.root:
            self.root=node
            return
        # 从上往下，从左往右的去遍历整棵树，然后找到第一个空位
        # 把节点添加进去
        queue=[self.root]  #存每一层的节点
        while True:
            # 第一次 queue=[root]
            # 第二次 queue=[root.left,root.left]
            # queue=[root.right,root.left.left,root.left.right]
            # queue=[ root.left.left , root.left.right , root.right.left , root.right.right]
            cur_node=queue.pop(0)
            # 先找左边看看有没有空位
            if not cur_node.left:
                cur_node.left=node
                return
            # 左边没有空位，找右边
            elif not cur_node.right:
                cur_node.right=node
                return
#             如果都没有空位，就把左边节点与右边节点都加到之后要判断的节点中
            queue.extend((cur_node.left,cur_node.right))

# 通过广度优先遍历来实现
    def show(self):
        if not self.root:
            return
        queue = [self.root]  # 存每一层的节点
        i=1
        while queue:
            size=len(queue)
            print(f"第{i}层",end="\t")
            for i in range(size):
                node=queue.pop(0)
                print(node.val,end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print()
            i+=1

# 通过深度遍历来实现
    def preorder(self):
        # 先序遍历，前序遍历 根节点-->左子树-->右子树
        def helper(root):
            if not root:
                return
            print(root.val,end=" ") # 输出根节点
            helper(root.left) #先序遍历左子树
            helper(root.right) #先序遍历右子树
        helper(self.root)
        print()

    def inorder(self):
#         中序遍历  左子树 根 右子树
        def helper(root):
            if not root:
                return
            helper(root.left) #先序遍历左子树
            print(root.val, end=" ")  # 输出根节点
            helper(root.right) #先序遍历右子树
        helper(self.root)
        print()

    def postorder(self):
#         后序遍历  左子树 右子树 根
        def helper(root):
            if not root:
                return
            helper(root.left) #先序遍历左子树
            helper(root.right) #先序遍历右子树
            print(root.val, end=" ")  # 输出根节点
        helper(self.root)
        print()

def buildTree(preorder,inorder):
    """
    根据前序遍历与中序遍历去构建一颗无重复节点的二叉树
    :param preorder:
    :param inorder:
    :return:
    """
#     递归结束条件
    if not preorder:
        return None
    in_idx=inorder.index(preorder[0]) #在中序遍历结果中找到根节点的索引
    root=Node(preorder[0])  #构建根节点
    root.left=buildTree(preorder[1:in_idx+1],inorder[:in_idx])  #构建左子树
    root.right=buildTree(preorder[in_idx+1:],inorder[in_idx+1:])
    return root
if __name__ == '__main__':
    tree=Tree()
    tree.root=buildTree(
        [0,1,3,7,8,4,9,2,5,6],
        [7,3,8,1,9,4,0,5,2,6]
    )
    tree.show()
    # tree.add(0)
    # tree.add(1)
    # tree.add(2)
    # tree.add(3)
    # tree.add(4)
    # tree.add(5)
    # tree.add(6)
    # tree.add(7)
    # tree.add(8)
    # tree.add(9)
    # tree.show()
    # tree.preorder()
    # tree.inorder()
    # tree.postorder()