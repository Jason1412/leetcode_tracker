# Last updated: 5/16/2026, 12:27:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        self.maxDepth = 0
        self.tgtVal = root.val

        self.dfs(root, 0)

        return self.tgtVal


    def dfs(self, root, depth):

        if root is None:
            return

        if not root.left and not root.right:
            if depth > self.maxDepth:
                self.maxDepth = depth
                self.tgtVal = root.val

        self.dfs(root.left, depth+1)
        self.dfs(root.right, depth+1)
                
