# Last updated: 5/16/2026, 12:26:48 PM
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1

        res = ''

        for char in order:
            if char in count:
                res += char * count[char]
                count[char] = 0

        for char, freq in count.items():
            if freq > 0:
                res += char * freq
            
        
        return res