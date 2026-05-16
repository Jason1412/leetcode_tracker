# Last updated: 5/16/2026, 12:26:57 PM
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        nrow, ncol = len(matrix), len(matrix[0])

        for i in range(nrow-1):
            for j in range(ncol-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return False

        return True


# Method 1 ====================================================
# My version
    # def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
    #     nrow, ncol = len(matrix), len(matrix[0])

    #     flag = True
    #     for i in range(nrow):
    #         if not self.check_identical((i, 0), matrix):
    #             flag = False
    #             return flag

    #     for j in range(1, ncol):
    #         if not self.check_identical((0, j), matrix):
    #             flag = False
    #             return flag

    #     return flag

        
    # def check_identical(self, posi, matrix):

    #     i, j = posi[0], posi[1]

    #     prev_val = matrix[i][j]

    #     i += 1
    #     j += 1

    #     while self.index_valid(i, j, matrix):
    #         if matrix[i][j] != prev_val:
    #             return False
    #         i += 1
    #         j += 1
    #     return True


    # def index_valid(self, i, j, matrix):
    #     nrow, ncol = len(matrix), len(matrix[0])

    #     if 0 <= i <= nrow - 1 and 0 <= j <= ncol - 1:
    #         return True
    #     else:
    #         return False