# Last updated: 5/22/2026, 2:47:44 PM
1class Solution:
2    def maximumGap(self, nums: List[int]) -> int:
3        
4        if len(nums) < 2:
5            return 0
6
7        nums.sort()
8
9        maxDiff = 0
10        
11
12        for i in range(1, len(nums)):
13            maxDiff = max(maxDiff, nums[i] - nums[i-1])
14
15        return maxDiff