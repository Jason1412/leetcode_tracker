# Last updated: 5/16/2026, 12:27:21 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            return TreeNode(val, left=root)


        self.dfs(root, val, 1, tgt_depth=depth)
        return root




    def dfs(self, root, val, depth, tgt_depth):

        if root is None:
            return 

        if depth == tgt_depth - 1:
            tmp = root.left
            root.left = TreeNode(val, left=tmp)

            tmp2 = root.right
            root.right = TreeNode(val, right=tmp2)

        self.dfs(root.left, val, depth+1, tgt_depth)
        self.dfs(root.right, val, depth+1, tgt_depth)

