# Last updated: 5/16/2026, 12:25:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        self.count = 0

        self.dfs(root)

        return self.count

    def dfs(self, root):

        if root is None:
            return 0, 0


        leftSum, leftCount = self.dfs(root.left)
        rightSum, rightCount = self.dfs(root.right)

        if (leftSum + root.val + rightSum) // (leftCount + 1 + rightCount) == root.val:
            self.count += 1

        return leftSum + root.val + rightSum, leftCount + 1 + rightCount