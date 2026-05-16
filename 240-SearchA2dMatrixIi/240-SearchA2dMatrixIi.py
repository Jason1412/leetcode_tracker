# Last updated: 5/16/2026, 12:28:43 PM
class Solution:
    
    def binary_search(self, array, target):
        # Returns the index of the nearest smaller element to target.
        
        if array is None or len(array) == 0:
            return -1
        
        left = 0
        right = len(array) - 1 
        
        while(left + 1 < right):
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid
            elif array[mid] > target:
                right = mid
        
        if array[right] <= target:
            return right
        elif array[left] >= target:
            return left
        elif array[left] < target and target < array[right]:
            return left

    def binary_search2(self, array, target):
        # Returns the index of the nearest smaller element to target.
        
        if array is None or len(array) == 0:
            return -1
        
        left = 0
        right = len(array) - 1 
        
        while(left + 1 < right):
            mid = left + (right - left) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                left = mid
            elif array[mid] > target:
                right = mid
        
        if array[left] == target:
            return True
        if array[right] == target:
            return True
        return False
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        ncol = len(matrix[0])
        nrow = len(matrix)
        
        col0 = [matrix[i][0] for i in range(nrow)]
        colN = [matrix[i][ncol-1] for i in range(nrow)]
        
        ind0 = self.binary_search(col0, target)
        indN = self.binary_search(colN, target)
        
        print(ind0)
        print(indN)
        out = False
        
        
        for i in range(indN, ind0+1):
            out = self.binary_search2(matrix[i], target)
            if out:
                return out 
            
        return out
        
        