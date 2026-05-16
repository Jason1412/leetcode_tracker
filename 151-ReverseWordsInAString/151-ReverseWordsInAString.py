# Last updated: 5/16/2026, 12:29:22 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        
        tmp = s.split(' ')

        tmp.reverse()

        return ' '.join([word for word in tmp if word])