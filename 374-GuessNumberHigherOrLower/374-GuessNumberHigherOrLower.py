# Last updated: 5/16/2026, 12:28:16 PM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n 
        
        if guess(start) == 0:
            return start
        
        if guess(end) == 0:
            return end
        
        while (start + 1 < end):
            mid = start + (end - start) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:   # num < mid
                end = mid
            elif guess(mid) == 1:
                start = mid
                
        if guess(start) == 0:
            return start
        elif guess(end) == 0:
            return end
        
        return -1
                