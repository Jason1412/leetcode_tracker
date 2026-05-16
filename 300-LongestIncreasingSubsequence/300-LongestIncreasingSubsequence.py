# Last updated: 5/16/2026, 12:28:34 PM
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            
            tmp = 0
            for j in range(0, i):
                if nums[i] > nums[j]:
                    tmp = max(tmp, dp[j])
                    
            dp[i] = tmp + 1
            






        print("dp=", dp)
        res = -1
        for item in dp:
            res = max(res, item)

        return res