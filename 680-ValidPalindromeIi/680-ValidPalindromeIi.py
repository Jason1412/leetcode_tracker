# Last updated: 5/16/2026, 12:27:10 PM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        start = 0
        end = len(s) - 1

        while (start < end):

            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return self.isPalind(s, start+1, end) or self.isPalind(s, start, end-1)
        return True
    

    def isPalind(self, s, start, end):

        start = start
        end = end

        while (start < end):
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False

        return True