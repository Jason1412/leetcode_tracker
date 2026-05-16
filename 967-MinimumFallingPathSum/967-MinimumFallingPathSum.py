# Last updated: 5/16/2026, 12:26:22 PM
import sys
class Solution:
# Method 3 ===================================================
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        memo = [[66666 for _ in range(n+2)] for _ in range(n)]

        for j in range(n):
            memo[0][j+1] = matrix[0][j]

        for i in range(1, n):
            for j in range(1,n+1):
                memo[i][j] = matrix[i][j-1] + min(memo[i-1][j-1],
                                                memo[i-1][j],
                                                memo[i-1][j+1])
        
        res = sys.maxsize

        for j in range(1, n+1):
            res = min(res, memo[n-1][j])

        return res
        





# Method 2 ====================================================
# Recursive + Memory
    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     n = len(matrix)
    #     res = sys.maxsize

    #     # define memo
    #     self.memo = [[66666 for _ in range(n)] for _ in range(n)]


    #     for j in range(n):
    #         res = min(res, self.dp(matrix, n-1, j))

    #     return res


    # def dp(self, matrix, i, j):
    #     n = len(matrix)

    #     if j < 0 or j > n-1:
    #         return 99999

    #     if i == 0:
    #         self.memo[0][j] = matrix[0][j]
    #         return matrix[0][j]

    #     if self.memo[i][j] != 66666:
    #         return self.memo[i][j]
    #     else:
    #         self.memo[i][j] = matrix[i][j] + min(self.dp(matrix, i-1, j-1),
    #                               self.dp(matrix, i-1, j),
    #                               self.dp(matrix, i-1, j+1))
    #     return self.memo[i][j]





# Method 1 ===================================================
# Recursive method

    # def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    #     n = len(matrix)
    #     res = sys.maxsize
        
    #     for j in range(n):
    #         res = min(res, self.dp(matrix, n-1, j))

    #     return res


    # def dp(self, matrix, i, j):
    #     n = len(matrix)

    #     if j < 0 or j > n-1:
    #         return 999

    #     if i == 0:
    #         return matrix[0][j]

        
    #     return matrix[i][j] + min(self.dp(matrix, i-1, j-1),
    #                               self.dp(matrix, i-1, j),
    #                               self.dp(matrix, i-1, j+1))



        