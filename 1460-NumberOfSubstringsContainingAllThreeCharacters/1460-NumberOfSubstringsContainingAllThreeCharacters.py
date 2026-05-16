# Last updated: 5/16/2026, 12:25:39 PM
from collections import Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        if len(s) < 3:
            return 0

        
        left = 0
        right = 0

        n = len(s)

        valid = 0
        need = Counter('abc')

        window = Counter()

        res = 0

        while right < n:
            char = s[right]
            right += 1

            window[char] += 1

            if window[char] == need[char]:
                valid += 1
            
            while valid == 3:
                res += n - (right - 1)

                d = s[left]
                left += 1

                window[d] -= 1
                
                if window[d] == 0:
                    valid -= 1

        return res

            

            



