# Last updated: 5/16/2026, 12:29:37 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        processed = []
        for char in s:
            if char.isalpha() or char.isdigit():
                processed.append(char.lower())
            
        s_p = ''.join(processed)

        if len(s_p) == 0:
            return True

        left = 0
        right = len(s_p) - 1

        while left < right:
            if s_p[left] == s_p[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
