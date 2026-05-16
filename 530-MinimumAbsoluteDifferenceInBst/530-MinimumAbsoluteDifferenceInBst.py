# Last updated: 5/16/2026, 12:27:41 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = []
        
        self.traversal(root)
        
        for i in range(len(self.result)-1):
            if i == 0:
                diff = abs(self.result[1] - self.result[0])
            diff = min(diff, abs(self.result[i+1] - self.result[i]))
        
        return diff
            
    
    def traversal(self, root):
        if root is None:
            return 
        
        self.traversal(root.left)
        self.result.append(root.val)
        self.traversal(root.right)