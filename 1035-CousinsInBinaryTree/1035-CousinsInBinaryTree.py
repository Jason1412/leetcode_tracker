# Last updated: 5/16/2026, 12:26:05 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        self.parentX = None
        self.parentY = None
        self.depthX = -1
        self.depthY = -1
        self.x = x
        self.y = y

        self.dfs(root, None, 0)

        if self.parentX and self.parentY and self.depthX == self.depthY:
            if self.parentX != self.parentY:
                return True

        return False




    def dfs(self, root, parent, depth):
        
        if root is None:
            return

        if root.val == self.x:
            self.parentX = parent
            self.depthX = depth
        
        if root.val == self.y:
            self.parentY = parent
            self.depthY = depth

        self.dfs(root.left, root, depth+1)
        self.dfs(root.right, root, depth+1)

        