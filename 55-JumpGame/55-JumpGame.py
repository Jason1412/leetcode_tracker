# Last updated: 5/16/2026, 12:30:25 PM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True

        start = 0
        end = 0
        max_range = 0
        i = 0
        while i < len(nums) and i <= end:
            max_range = max(max_range, nums[i]+i)
            if i == end:
                end = max_range
                start = i + 1

            i += 1

        
        if end >= len(nums)-1:
            return True
        else:
            return False