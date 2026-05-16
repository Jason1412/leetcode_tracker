# Last updated: 5/16/2026, 12:27:25 PM
class Solution:
    out = ''
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t is None:
            return ""
        
        if t.left is None and t.right is None:
            return str(t.val) + ""
        
        if t.right is None:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        
        return str(t.val) + "(" + self.tree2str(t.left) + ")(" + self.tree2str(t.right) + ")" 
    
    # first finish the divide and conquer process 
    # then deal with the special cases.