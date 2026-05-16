# Last updated: 5/16/2026, 12:30:32 PM
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        farthest = 0

        jumps = 0

        for i in range(n-1): # This is n-1, not n! 
            farthest = max(nums[i] + i, farthest)
            if end == i:
                jumps += 1
                end = farthest

        return jumps