# Last updated: 5/16/2026, 12:27:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        
        self.res = Counter()

        self.subtreeSum(root)

        top_count = self.res.most_common(1)[0][1]

        return [val for val, freq in self.res.most_common() if freq == top_count]


    def subtreeSum(self, root):

        if root is None:
            return 0

        
        leftSum = self.subtreeSum(root.left)
        rightSum = self.subtreeSum(root.right)

        treeSum = leftSum + rightSum + root.val

        self.res[treeSum] += 1

        return treeSum
