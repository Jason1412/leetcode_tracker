# Last updated: 5/16/2026, 12:30:18 PM
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        f0 = 1
        f1 = 2
        
        for i in range(3, n+1):
            f = f0 + f1
            f1, f0 = f, f1
        
        return f