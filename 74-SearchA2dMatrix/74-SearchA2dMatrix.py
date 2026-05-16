# Last updated: 5/16/2026, 12:30:14 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if matrix is None or len(matrix) == 0:
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        
        left = 0
        right = col * row - 1
        
        while(left <= right):
            mid = left + (right - left) // 2
            
            ind_col = mid % col
            ind_row = mid // col
            
            if matrix[ind_row][ind_col] == target:
                return True
            elif matrix[ind_row][ind_col] < target:
                left = mid + 1
            elif matrix[ind_row][ind_col] > target:
                right = mid - 1 
        
        
        return False