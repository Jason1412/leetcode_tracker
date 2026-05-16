# Last updated: 5/16/2026, 12:27:04 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        preSum = [0 for _ in range(n+1)]

        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]

        
        for i in range(1, n+1):
            
            if preSum[i-1] == preSum[-1] - preSum[i]:
                return i-1

        
        if preSum[-2] == 0:
            return n-1

        return -1
