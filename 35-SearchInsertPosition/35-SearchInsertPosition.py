# Last updated: 5/16/2026, 12:30:37 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        start = 0 
        end = len(nums) - 1
        
        while (start + 1 < end):
            mid = start + (end - start)//2 
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                end = mid
            elif nums[mid] < target:
                start = mid
                
        print("target=", target)
        print("nums[start]=", nums[start])
        print("nums[end]=", nums[end])        
        if target == nums[start]:
            return start
        elif target > nums[start]:
            return end

