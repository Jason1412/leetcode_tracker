# Last updated: 5/16/2026, 12:30:42 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n1, n2 = len(haystack), len(needle)

        if n2 > n1:
            return -1

        for i in range(n1-n2+1):
            if haystack[i:i+n2] == needle:
                return i
        
        return -1