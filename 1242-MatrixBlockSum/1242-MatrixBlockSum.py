# Last updated: 5/16/2026, 12:25:50 PM
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        preSumMat = NumMatrix(mat)

        nrow, ncol = len(mat), len(mat[0])

        
        for i in range(nrow):
            for j in range(ncol):
                x1, y1, x2, y2 = self.find_index_pair(i, j, k, nrow, ncol)

                mat[i][j] = preSumMat.sumRegion(x1, y1, x2, y2)

        return mat


    def find_index_pair(self, i, j, k, nrow, ncol):

        x1 = i - k
        y1 = j - k

        x2 = i + k
        y2 = j + k

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0

        if x2 > nrow - 1:
            x2 = nrow - 1
        if y2 > ncol - 1:
            y2 = ncol - 1

        return x1, y1, x2, y2



class NumMatrix:
    def __init__(self, matrix):

        m, n = len(matrix), len(matrix[0])

        self.preSum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m+1):
            for j in range(n+1):
                self.preSum[i][j] = self.preSum[i-1][j] + \
                    + self.preSum[i][j-1] + matrix[i-1][j-1] - self.preSum[i-1][j-1] 


    def sumRegion(self, x1, y1, x2, y2):

        return self.preSum[x2+1][y2+1] - self.preSum[x2+1][y1] \
        - self.preSum[x1][y2+1] + self.preSum[x1][y1]