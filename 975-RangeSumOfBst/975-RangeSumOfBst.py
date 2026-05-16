# Last updated: 5/16/2026, 12:26:20 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.out = []

        self.dfs(root, low, high)
        return sum(self.out)
    
    def dfs(self, root, low, high):

        if not root:
            return

        if low <= root.val <= high:
            self.out.append(root.val)
            self.dfs(root.left, low, high)
            self.dfs(root.right, low, high)

        if root.val < low:
            self.dfs(root.right, low, high)

        if high < root.val:
            self.dfs(root.left, low, high)
        
