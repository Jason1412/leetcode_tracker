# Last updated: 5/16/2026, 12:26:00 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0
        self.path = 0

        self.dfs(root)

        return self.res


    def dfs(self, root):
        
        if root is None:
            return


        
        self.path = self.path << 1 | root.val

        if not root.left and not root.right:
            self.res += self.path

        self.dfs(root.left)
        self.dfs(root.right)

        self.path = self.path >> 1