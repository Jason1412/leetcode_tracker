# Last updated: 5/16/2026, 12:28:40 PM
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        left = 1
        
        right = n
        
        if isBadVersion(right) is False:
            return -1
        if isBadVersion(left) is True:
            return left
        
        while(left + 1 < right):
            mid = left + (right - left) // 2
            
            if isBadVersion(mid) is True:
                right = mid
            elif isBadVersion(mid) is False:
                left = mid
                
        if isBadVersion(left) is True:
            return left
        if isBadVersion(right) is True:
            return right
        return -1 