# Last updated: 5/16/2026, 12:27:58 PM
class Solution:
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        left = 0
        i = 0
        
        while i < len(chars):
            char = chars[i]
            f = 1
            while (i+1 < len(chars) and chars[i] == chars[i+1]):
                f += 1
                i += 1
                
            chars[left] = char
            if f > 1:
                len_str = str(f)
                for j in range(len(len_str)):
                    chars[left + j + 1] = len_str[j]
                left = left + len(len_str) + 1
                i += 1
            else:
                left = left + 1
                i += 1
        return left