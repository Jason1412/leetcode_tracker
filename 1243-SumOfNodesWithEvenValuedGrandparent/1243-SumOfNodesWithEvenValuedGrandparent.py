# Last updated: 5/16/2026, 12:25:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0

        self.dfs(root)
        
        return self.res

    def dfs(self, root):

        if root is None:
            return

        if root.val % 2 == 0:
            if root.left and root.left.left:
                self.res += root.left.left.val
            if root.left and root.left.right:
                self.res += root.left.right.val

            if root.right and root.right.left:
                self.res += root.right.left.val
            if root.right and root.right.right:
                self.res += root.right.right.val
        

        self.dfs(root.left)
        self.dfs(root.right)