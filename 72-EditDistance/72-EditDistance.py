# Last updated: 5/16/2026, 12:30:15 PM
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        self.memo = [[-1 for _ in range(n2)] for _ in range(n1)]

        return self.dp(word1, n1-1, word2, n2-1)

    def dp(self, word1, i, word2, j):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        if self.memo[i][j] != -1:
            return self.memo[i][j]


        if word1[i] == word2[j]:
            res = self.dp(word1, i-1, word2, j-1)
        else:
            res = min(self.dp(word1, i-1, word2, j),
                       self.dp(word1, i-1, word2, j-1),
                       self.dp(word1, i, word2, j-1)) + 1
        
        self.memo[i][j] = res
        
        return self.memo[i][j]


# Method 2 =====================================================
# Recursion
    # def minDistance(self, word1: str, word2: str) -> int:
    #     n1 = len(word1)
    #     n2 = len(word2)

    #     return self.dp(word1, n1-1, word2, n2-1)

    # def dp(self, word1, i, word2, j):
    #     if i == -1:
    #         return j + 1
    #     if j == -1:
    #         return i + 1
        
    #     if word1[i] == word2[j]:
    #         res = self.dp(word1, i-1, word2, j-1)
    #     else:
    #         res = min(self.dp(word1, i-1, word2, j),
    #                    self.dp(word1, i-1, word2, j-1),
    #                    self.dp(word1, i, word2, j-1)) + 1
    #     return res


# Method 3 ========================================================
# DP table
    # def minDistance(self, word1: str, word2: str) -> int:
    #     n1 = len(word1) # row
    #     n2 = len(word2) # col

    #     dp = [[-1 for _ in range(n2+1)] for _ in range(n1+1)]

    #     for i in range(n2+1):
    #         dp[0][i] = i
        
    #     for i in range(1, n1+1):
    #         dp[i][0] = i

    #     for i in range(1, n1+1):
    #         for j in range(1, n2+1):
    #             if word1[i-1] == word2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = min(dp[i-1][j-1], 
    #                            dp[i-1][j],
    #                            dp[i][j-1]) + 1
    #     print("dp=", dp)
    #     return dp[n1][n2]