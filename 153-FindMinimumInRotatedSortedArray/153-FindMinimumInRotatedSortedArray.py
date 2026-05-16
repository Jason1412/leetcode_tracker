# Last updated: 5/16/2026, 12:29:20 PM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1

        if nums[end] >= nums[start]:
            return nums[start]


        while (start + 1 < end):
            mid = (start + end) // 2
            
            if nums[mid] > nums[start]:
                start = mid 
            elif nums[mid] < nums[start]:
                end = mid
            elif nums[mid] == nums[start]:
                end = mid
        
        if nums[start] > nums[end]:
            return nums[end]
        else:
            return nums[start]