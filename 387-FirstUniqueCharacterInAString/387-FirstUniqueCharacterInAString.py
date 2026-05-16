# Last updated: 5/16/2026, 12:28:11 PM
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        rec = collections.Counter(s)
        
        for i in range(len(s)):
            if s[i] in rec and rec[s[i]] == 1:
                return i
        
        return -1