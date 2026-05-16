# Last updated: 5/16/2026, 12:27:43 PM
from collections import Counter
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1

        
        preSum = {}
        running_sum = 0
        max_len = 0
        preSum[0] = -1

        for i in range(len(nums)):
            running_sum += nums[i]
            if running_sum not in preSum:
                preSum[running_sum] = i
            else:
                max_len = max(max_len, i - preSum[running_sum])

        return max_len
            