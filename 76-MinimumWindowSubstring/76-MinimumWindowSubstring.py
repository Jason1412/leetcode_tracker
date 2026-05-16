# Last updated: 5/16/2026, 12:30:12 PM
from collections import Counter
import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        
        if len(t) > len(s):
            return ""

        dict_t = Counter(t)
        window = Counter()

        left, right = 0, 0
        valid = 0

        res = ""
        length = sys.maxsize

        while right < len(s):
            c = s[right]
            right += 1
            if c in dict_t:
                window[c] += 1

                if window[c] == dict_t[c]:
                    valid += 1
                
            
            while valid == len(dict_t):
                
                if (right - left) < length:
                    res = s[left:right]
                    length = (right - left)

                
                d = s[left]

                left += 1

                if d in dict_t:
                    window[d] -= 1
                    if window[d] < dict_t[d]:
                        valid -= 1

        return res