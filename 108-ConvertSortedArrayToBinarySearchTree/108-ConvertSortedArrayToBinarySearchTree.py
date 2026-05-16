# Last updated: 5/16/2026, 12:29:52 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.build(nums, 0, len(nums)-1)

    def build(self, nums, start, end):

        if start > end:
            return
        

        mid = (start + end) // 2

        root = TreeNode(nums[mid])

        root.left = self.build(nums, start, mid-1)
        root.right = self.build(nums, mid+1, end)

        return root
