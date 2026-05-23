# Last updated: 5/23/2026, 4:24:08 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        
4        start, end = 0, len(nums) - 1
5
6        while start + 1 < end:
7            mid = start + (end - start) // 2
8            if nums[mid] < target:
9                start = mid
10            elif nums[mid] > target:
11                end = mid
12            elif nums[mid] == target:
13                return mid
14
15
16        if nums[start] == target:
17            return start
18        elif nums[end] == target:
19            return end
20        else:
21            return -1