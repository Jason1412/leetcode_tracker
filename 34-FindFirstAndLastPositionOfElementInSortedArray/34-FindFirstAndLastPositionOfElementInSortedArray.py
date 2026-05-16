# Last updated: 5/16/2026, 12:30:39 PM
class Solution:
    def binary_search_left(self, nums, target):
        
        if nums is None or len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while(left+1 < right):
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                right = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
                
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        
        return -1
    
    def binary_search_right(self, nums, target):
        
        if nums is None or len(nums) == 0:
            return -1
        
        left = 0
        right = len(nums) - 1
        
        while(left+1 < right):
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                left = mid
            elif nums[mid] < target:
                left = mid
            elif nums[mid] > target:
                right = mid
                
        
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        
        return -1    
        
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        return [self.binary_search_left(nums, target), self.binary_search_right(nums, target)]