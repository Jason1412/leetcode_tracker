# Last updated: 5/16/2026, 12:28:24 PM
class Solution:
    def integerBreak(self, n: int) -> int:
        M = [0 for i in range(n+1)]
        M[1] = 0
        
        for i in range(2, n+1):
            curMax = 0
            
            for j in range(1, i):
                curMax = max(curMax, max(j, M[j]) * (i-j))
            
            M[i] = curMax
            
        return M[-1]
                
            