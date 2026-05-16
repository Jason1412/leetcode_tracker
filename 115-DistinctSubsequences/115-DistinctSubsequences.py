# Last updated: 5/16/2026, 12:29:45 PM
class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        # f[i][j] - the first i chars in s
        #         - the first j chars in t
        
        n_s = len(s)
        n_t = len(t)
        
        dp = [[0]*(n_t+1) for i in range(n_s+1)]
        
        for i in range(len(s)):
            dp[i][0] = 1
        
        for i in range(n_s):
            for j in range(n_t):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j+1] + dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i][j+1]
                    
        return dp[n_s][n_t]