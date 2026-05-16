# Last updated: 5/16/2026, 12:27:06 PM
class Solution:
# Method 3 ==================================================
# recursion + memo
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        self.memo = [[-1 for _ in range(n2)] for _ in range(n1)]

        return self.dp(s1, 0, s2, 0)

    # dp(i, j) --- s1[i...], s2[j...]

    def dp(self, s1, i, s2, j):
        res = 0
        if i == len(s1):
            res = sum([ord(x) for x in s2[j:]])
            return res
        if j == len(s2):
            res = sum([ord(x) for x in s1[i:]])
            return res

        if self.memo[i][j] != -1:
            return self.memo[i][j]

        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i+1, s2, j+1)
        else:
            self.memo[i][j] = min(self.dp(s1, i+1, s2, j) + ord(s1[i]),
            self.dp(s1, i, s2, j+1) + ord(s2[j]))

        return self.memo[i][j]


# Method 2 =====================================================
# recursion
    # def minimumDeleteSum(self, s1: str, s2: str) -> int:
    #     n1 = len(s1)
    #     n2 = len(s2)


    #     return self.dp(s1, 0, s2, 0)

    # # dp(i, j) --- s1[i...], s2[j...]

    # def dp(self, s1, i, s2, j):
    #     res = 0
    #     if i == len(s1):
    #         res = sum([ord(x) for x in s2[j:]])
    #         return res
    #     if j == len(s2):
    #         res = sum([ord(x) for x in s1[i:]])
    #         return res


    #     if s1[i] == s2[j]:
    #         return self.dp(s1, i+1, s2, j+1)
    #     else:
    #         return min(self.dp(s1, i+1, s2, j) + ord(s1[i]),
    #         self.dp(s1, i, s2, j+1) + ord(s2[j]))

    

        



# Method 1 =====================================================
# dp table
    # def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
    #     n1 = len(s1)
    #     n2 = len(s2)

    #     dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

    #     for i in range(1, n1+1):
    #         dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
    #     for j in range(1, n2+1):
    #         dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        
    #     for i in range(1, n1+1):
    #         for j in range(1, n2+1):
    #             if s1[i-1] == s2[j-1]:
    #                 dp[i][j] = dp[i-1][j-1]
    #             else:
    #                 dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]),
    #                             dp[i][j-1] + ord(s2[j-1]))

    #     return dp[n1][n2]
                    