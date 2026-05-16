# Last updated: 5/16/2026, 12:26:06 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.track = []
        self.min_str = None

        self.dfs(root)

        return self.min_str
        

    def dfs(self, root):
        if root is None:
            return 


        self.track.append(self.mapping(root.val))

        if not root.left and not root.right:
            s = ''.join(self.track[::-1])
            if not self.min_str or self.min_str > s:
                self.min_str = s

        self.dfs(root.left)
        self.dfs(root.right)

        self.track.pop()

    def mapping(self, intVal):

        string = 'abcdefghijklmnopqrstuvwxyz'
        return string[intVal]