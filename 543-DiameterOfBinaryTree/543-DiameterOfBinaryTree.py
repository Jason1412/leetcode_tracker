# Last updated: 5/16/2026, 12:27:36 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.max_len = 0

        self.dfs(root)

        return self.max_len

    def dfs(self, root):

        if root is None:
            return 0

        left_len = self.dfs(root.left)
        right_len = self.dfs(root.right)

        self.max_len = max(self.max_len, left_len + right_len)

        return max(left_len, right_len) + 1