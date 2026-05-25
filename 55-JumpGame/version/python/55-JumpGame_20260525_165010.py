# Last updated: 5/25/2026, 4:50:10 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        
4        n = len(nums)
5        farthest = 0
6        for i in range(n - 1):
7            # 不断计算能跳到的最远距离
8            farthest = max(farthest, i + nums[i])
9            # 可能碰到了 0，卡住跳不动了
10            if farthest <= i:
11                return False
12        return farthest >= n - 1