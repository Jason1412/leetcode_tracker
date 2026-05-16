# Last updated: 5/16/2026, 12:28:18 PM
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        start = 1
        end = num
        
        while (start + 1 < end):
            mid = (end - start) // 2 + start
            print("mid=",mid)
            if mid**2 == num:
                return True
            elif mid**2 > num:
                end = mid
            elif mid**2 < num:
                start = mid
            
        if start**2 == num:
            return True
        if end**2 == num:
            return True
        
        return False