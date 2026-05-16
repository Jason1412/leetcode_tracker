# Last updated: 5/16/2026, 12:25:48 PM
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n1][n2]
        



# Method 2 ==========================================================
# Recursion + Memo
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
    #     self.memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        

    #     return self.dp(text1, 0, text2, 0)

    # def dp(self, text1, i, text2, j):
    #     if i == len(text1):
    #         return 0
    #     if j == len(text2):
    #         return 0

    #     # print("i={}, j={}".format(i, j))
    #     if self.memo[i][j] != -1:
    #         return self.memo[i][j]

    #     if text1[i] != text2[j]:
    #         self.memo[i][j] = max(self.dp(text1, i+1, text2, j),
    #                    self.dp(text1, i, text2, j+1))
    #     else:
    #         self.memo[i][j] = self.dp(text1, i+1, text2, j+1)+1      
        
    #     return self.memo[i][j]


# Method 1 ==========================================================
# Recursion
    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        

    #     return self.dp(text1, 0, text2, 0)

    # def dp(self, text1, i, text2, j):
    #     if i == len(text1):
    #         return 0
    #     if j == len(text2):
    #         return 0

    #     if text1[i] != text2[j]:
    #         return max(self.dp(text1, i+1, text2, j),
    #                    self.dp(text1, i, text2, j+1))

    #     else:
    #         return self.dp(text1, i+1, text2, j+1)+1