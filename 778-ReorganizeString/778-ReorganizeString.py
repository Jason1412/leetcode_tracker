# Last updated: 5/16/2026, 12:26:55 PM
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        s_dict = Counter(s)
        print(s_dict.most_common(1))
        
        tmp = s_dict.most_common(1)
        most_char, most_freq = tmp[0][0], tmp[0][1]
        
        if len(s) % 2 == 0:
                
            if most_freq > len(s) // 2:
                return ""
        else:
            if most_freq > len(s) // 2 + 1:
                return ""
        
        len_rest = len(s) - most_freq

        out = [[most_char] for _ in range(most_freq)]


        pos = 0
        for char, count in s_dict.items():
            if char == most_char:
                continue

            for i in range(count):
                out[pos % most_freq].append(char)
                pos += 1
        
        return ''.join([''.join(item) for item in out])

            
