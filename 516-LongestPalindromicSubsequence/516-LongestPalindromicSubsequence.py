# Last updated: 5/16/2026, 12:27:47 PM
class Solution:
# Method 2 ====================================================
    def longestPalindromeSubseq(self, s: str) -> int:
        
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        # base case 
        for i in range(n):
            dp[i][i] = 1

        for k in range(1, n):
            i = 0
            j = k
            while j <= n-1:
                
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                i += 1
                j += 1
        return dp[0][n-1]  


# Method 1 ====================================================
    # def longestPalindromeSubseq(self, s: str) -> int:
        
    #     n = len(s)
    #     dp = [[0 for _ in range(n)] for _ in range(n)]

    #     # base case 
    #     for i in range(n):
    #         dp[i][i] = 1

    #     for i in range(n-2, -1, -1):
    #         for j in range(i+1, n):
    #             if s[i] == s[j]:
    #                 dp[i][j] = dp[i+1][j-1] + 2
    #             else:
    #                 dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    #     return dp[0][n-1]
