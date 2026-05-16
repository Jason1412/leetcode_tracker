# Last updated: 5/16/2026, 12:27:11 PM
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        longest, incr = 1, 1

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                incr += 1
            elif nums[i-1] >= nums[i]:
                incr = 1

            longest = max(incr, longest)

        return longest