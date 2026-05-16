# Last updated: 5/16/2026, 12:27:38 PM
class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s_list = list(s)
        
        for i in range(0, len(s), 2*k):
            s_list[i:i+k] = reversed(s_list[i:i+k])
        
        return ''.join(s_list)