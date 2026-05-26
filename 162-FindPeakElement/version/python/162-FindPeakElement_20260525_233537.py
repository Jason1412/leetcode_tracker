# Last updated: 5/25/2026, 11:35:37 PM
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        
4        left, right = 0, len(nums) - 1
5
6        while left + 1 < right:
7            mid = left + (right - left) // 2
8
9            if nums[mid] > nums[mid+1]:
10                right = mid
11            else:
12                left = mid
13
14        if nums[left] < nums[right]:
15            return right
16
17        else:
18            return left