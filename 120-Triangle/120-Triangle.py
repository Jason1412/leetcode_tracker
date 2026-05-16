# Last updated: 5/16/2026, 12:29:43 PM

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        f = [[float('inf')]*i for i in range(1,len(triangle)+1)]

        f[0][0] = triangle[0][0]

        for i in range(1,n):
            for j in range(len(f[i])):
                if j - 1 >= 0:
                    f[i][j] = min(f[i][j], f[i-1][j-1])
                if j < len(f[i-1]):
                    f[i][j] = min(f[i][j], f[i-1][j])
                
                f[i][j] += triangle[i][j]
        
        return min(f[n-1])
