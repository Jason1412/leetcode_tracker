# Last updated: 5/16/2026, 12:28:08 PM
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = Counter(s)
        
        count = 0
        single_count = 0
        max_single_count = 0

        # print(res)

        for key, val in res.items():
            if val % 2 == 1:
                if single_count == 0:
                    single_count += 1
                
                count += val - 1
            
            if val % 2 == 0:
                count += val
            # print("===========")
            # print(count)
            # print(max_single_count)
       

        if single_count > 0:
            return count + 1

        return count
