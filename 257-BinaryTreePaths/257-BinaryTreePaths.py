# Last updated: 5/16/2026, 12:28:38 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        self.track = []
        self.res = []

        self.dfs(root)

        return self.res




    def dfs(self, root):
        if root is None:
            return
    
        
        self.track.append(str(root.val))

        if not root.left and not root.right:
            self.res.append('->'.join(self.track))

        self.dfs(root.left)
        self.dfs(root.right)

        self.track.pop()

