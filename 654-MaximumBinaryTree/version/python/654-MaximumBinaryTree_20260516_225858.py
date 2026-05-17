# Last updated: 5/16/2026, 10:58:58 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
9        return self.build(nums, 0, len(nums)-1)
10
11
12    def build(self, nums, lo, hi):
13
14        if lo > hi:
15            return None
16
17        maxVal = float('-inf')
18        index = -1
19
20        for i in range(lo, hi+1):
21            if nums[i] > maxVal:
22                maxVal = nums[i]
23                index = i
24            
25        root = TreeNode(maxVal)
26
27        left = self.build(nums, lo, index-1)
28        right = self.build(nums, index+1, hi)
29
30        root.left = left
31        root.right = right
32
33        return root
34