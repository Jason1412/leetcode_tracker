# Last updated: 5/16/2026, 12:30:54 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        max_len = 0
        res = None

        for i in range(len(s)):
            start, end = self.findPalindrome(s, i, i)

            if end - start + 1 > max_len:
                max_len = end - start + 1
                res = s[start: end+1]
            
            start, end = self.findPalindrome(s, i, i+1)

            if end - start + 1 > max_len:
                max_len = end - start + 1
                res = s[start: end+1]

        return res




    def findPalindrome(self, s, left, right):
        

        while left >= 0 and right <= len(s) - 1:
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                return left + 1, right - 1
        
        if left < 0:
            return 0, right - 1
        
        if right > len(s) - 1:
            return left + 1, right

        
        