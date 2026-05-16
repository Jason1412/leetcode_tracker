# Last updated: 5/16/2026, 12:30:19 PM
class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        start = 1
        end = x
        
        while (start + 1) < end:
            mid = (end - start) // 2 + start
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                start = mid
            elif x < mid**2:
                end = mid
                
        if start**2 == x:
            return start
        if end**2 == x:
            return end
        
        return start
        
        
        