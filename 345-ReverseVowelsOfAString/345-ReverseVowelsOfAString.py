# Last updated: 5/16/2026, 12:28:22 PM
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = set('aeiouAEIOU')
        start = 0
        end = len(s) - 1
        s_list = list(s)
        
        while start < end:
         
            while start < end and s_list[end] not in vowel:
                end -= 1
            while start < end and s_list[start] not in vowel:
                start += 1
            
            s_list[start], s_list[end] = s_list[end], s_list[start]
            start += 1
            end -=1
        
        return ''.join(s_list)
            
            