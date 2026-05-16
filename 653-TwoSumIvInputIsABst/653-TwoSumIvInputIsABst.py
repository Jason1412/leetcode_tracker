# Last updated: 5/16/2026, 12:27:17 PM
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return
        
        res = []
        
        self.traversal(root, res)
        
        start = 0
        end = len(res) - 1
        
        while start < end:
            if res[start] + res[end] == k:
                return True
            elif res[start] + res[end] < k:
                start += 1
            else:
                end -= 1
        return False
        
    def traversal(self, root, res):
        
        if root is None:
            return
        
        self.traversal(root.left, res)
        res.append(root.val)
        self.traversal(root.right, res)
        
        return
        