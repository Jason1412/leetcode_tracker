# Last updated: 5/16/2026, 12:27:24 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 is None:
            return root2
        # 遍历 root1，顺便把 root2 的节点合并过来
        self.traverse(root1, root2)
        return root1

    def traverse(self, root1: TreeNode, root2: TreeNode):
        if root1 is None or root2 is None:
            return
        if root1 is not None and root2 is not None:
            # 两棵树都有的节点，叠加节点值
            root1.val += root2.val
        # 如果 root1 没有子树而 root2 有，那么就把 root2 的子树接到 root1 上
        # 注意接完之后把 root2 的子树置为 null，免得错误计算节点累加值
        if root1.left is None and root2.left is not None:
            root1.left = root2.left
            root2.left = None
            
        if root1.right is None and root2.right is not None:
            root1.right = root2.right
            root2.right = None
            
        # 递归遍历左右子节点，root2 的节点也跟着同步移动
        self.traverse(root1.left, root2.left)
        self.traverse(root1.right, root2.right)