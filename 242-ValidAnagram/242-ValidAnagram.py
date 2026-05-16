# Last updated: 5/16/2026, 12:28:41 PM
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)


        for key, val in s_dict.items():
            if key not in t_dict:
                return False

            if s_dict[key] != t_dict[key]:
                return False


        return True