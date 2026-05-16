# Last updated: 5/16/2026, 12:28:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


# Wrong version: 
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        self.path_sum = 0
        self.res = 0
        self.preSum = {}
        self.preSum[0] = 1

        self.dfs(root, targetSum)

        return self.res


    def dfs(self, root, targetSum):

        if root is None:
            return

        
        self.path_sum += root.val

        num = self.path_sum - targetSum

        if num in self.preSum:
            self.res += self.preSum[num]

        self.preSum[self.path_sum] = self.preSum.get(self.path_sum, 0) + 1

        self.dfs(root.left, targetSum)
        self.dfs(root.right, targetSum)        

        self.preSum[self.path_sum] = self.preSum.get(self.path_sum, 0) - 1
        self.path_sum -= root.val

