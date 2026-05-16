# Last updated: 5/16/2026, 12:27:34 PM
class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_word = s.split()
        
        out = []
        for word in list_word:
            tmp = word[::-1]
            out += [tmp]
        
        return " ".join(out)
        