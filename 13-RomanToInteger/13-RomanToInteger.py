# Last updated: 5/16/2026, 12:30:53 PM
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        out = 0
        
        for i in range(len(s)):
            if i == len(s)-1:
                out += val_dict[s[i]]
                break
            
            if val_dict[s[i]] < val_dict[s[i+1]]:
                out += - val_dict[s[i]]
            else:
                out += val_dict[s[i]]
        return out
