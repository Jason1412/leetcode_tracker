# Last updated: 5/16/2026, 12:29:39 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.max_val = - sys.maxsize

        self.singleMax(root)
        return self.max_val


    def singleMax(self, root):

        if root is None:
            return 0

        leftMax = self.singleMax(root.left)
        rightMax = self.singleMax(root.right)

        # 在求解path_sum以及return的时候, 都需要trim <0的subtree, 所以需要在这里
        # 做一下处理, 而不能
        #         path_sum = max(root.val, 
                    #    root.val + leftMax,
                    #    root.val + rightMax,
                    #    root.val + leftMax + rightMax)
        if leftMax < 0:
            leftMax = 0

        if rightMax < 0:
            rightMax = 0

        # path_sum = max(root.val + leftMax,
        #                root.val + rightMax,
        #                root.val + leftMax + rightMax)

        path_sum = root.val + leftMax + rightMax
        self.max_val = max(self.max_val, path_sum)


        return root.val + max(leftMax, rightMax)


# # For mutated version =======================================
# import sys
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
#         self.maxSum = - sys.maxsize

#         self.find_sum(root)

#         return self.maxSum

#     def find_sum(self, root):

#         if root is None:
#             return 0
        

#         left_sum = self.find_sum(root.left)
#         right_sum = self.find_sum(root.right)

#         self.maxSum = max(self.maxSum, left_sum + right_sum + root.val)
        
#         return max(left_sum + root.val, right_sum + root.val)

        
