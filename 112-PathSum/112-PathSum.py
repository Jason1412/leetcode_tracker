# Last updated: 5/16/2026, 12:29:49 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: 
        if root is None:
            return False
        
        return self.dfs(root, targetSum)


    def dfs(self, root, count):

        # if root is None:
        #     return False
        if root is None:
            return False

        if root.left is None and root.right is None:
            if count == root.val:
                return True
            else:
                return False

        if root.left:
            if self.dfs(root.left, count-root.val):
                return True
        
        if root.right:
            if self.dfs(root.right, count-root.val):
                return True

        return False
        






# Method 1 =========================================================
# Recursion based on traverse
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:     
    #     if not root:
    #         return False
        
    #     self.res = False

    #     self.dfs(root, 0, targetSum)

    #     return self.res
    


    # def dfs(self, root, cumSum, targetSum):

    #     if root is None:
    #         return 
        
    #     if self.res:
    #         return
        
    #     cumSum += root.val
    #     if not root.left and not root.right and cumSum == targetSum:
    #         self.res = True
            
    #     self.dfs(root.left, cumSum, targetSum)
    #     self.dfs(root.right, cumSum, targetSum)

    #     cumSum -= root.val