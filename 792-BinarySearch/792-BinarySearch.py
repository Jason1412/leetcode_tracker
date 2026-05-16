# Last updated: 5/16/2026, 12:26:52 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while (start + 1 < end):
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1

        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end

        return -1