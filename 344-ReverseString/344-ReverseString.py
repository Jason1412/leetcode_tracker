# Last updated: 5/16/2026, 12:28:23 PM
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        
        tmp = []
        for i in range(n-1, -1, -1):
            tmp += [s[i]]
        
        return ''.join(tmp)