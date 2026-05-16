# Last updated: 5/16/2026, 12:27:45 PM
class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        len_a = len(a)
        len_b = len(b)
        
        if a == b:
            return -1
        else:
            return max(len_a, len_b)
            