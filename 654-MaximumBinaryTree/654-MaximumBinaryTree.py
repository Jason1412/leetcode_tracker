# Last updated: 5/16/2026, 12:27:16 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        root = self.build(nums, 0, len(nums)-1)
        return root
        

    def build(self, nums, start, end):

        if start > end:
            return

        
        ind = -1
        max_val = -1

        for i in range(start, end+1):
            if nums[i] > max_val:
                max_val = nums[i]
                ind = i
        
        root = TreeNode(max_val)

        root.left = self.build(nums, start, ind-1)
        root.right = self.build(nums, ind+1, end)

        return root