# Last updated: 5/16/2026, 12:30:36 PM
class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"

        
        tmp = self.countAndSay(n-1)

        left, right = 0, 0

        out = []

        while left < len(tmp) and right < len(tmp):

            while right < len(tmp) and tmp[left] == tmp[right]:
                right += 1
            
            out.append(str(right - left) + tmp[left])
            
            left = right
        
        return "".join(out)
    