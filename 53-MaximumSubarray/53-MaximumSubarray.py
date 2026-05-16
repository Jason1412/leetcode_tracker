# Last updated: 5/16/2026, 12:30:26 PM
import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-20000 for _ in nums]

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i-1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]


        
        res = -sys.maxsize

        for item in dp:
            res = max(res, item)
        return res








# Method 1: Two Pointers ========================================
    # def maxSubArray(self, nums: List[int]) -> int:
    #     left, right = 0, 0
    #     windowSum = 0
    #     maxSum = -sys.maxsize

    #     while (right < len(nums)):
    #         windowSum += nums[right]
    #         right += 1

    #         if windowSum > maxSum:
    #             maxSum = windowSum

    #         while (windowSum < 0):
    #             windowSum -= nums[left]
    #             left += 1

    #     return maxSum