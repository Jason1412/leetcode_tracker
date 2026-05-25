# Last updated: 5/25/2026, 2:44:54 PM
1import random
2class Solution:
3    def findKthLargest(self, nums: List[int], k: int) -> int:
4        
5        random.shuffle(nums)
6
7        left, right = 0, len(nums) - 1
8        k_p = len(nums) - k
9
10        while left <= right:
11
12            p = self.partition(nums, left, right)
13
14            if p < k_p:
15                left = p + 1
16
17            elif p > k_p:
18                right = p - 1
19
20            else:
21                return nums[p]
22
23        return -1
24
25
26    def partition(self, nums, start, end):
27
28        left = start + 1
29        right = end
30
31        pivot = nums[start]
32
33        while left <= right:
34
35            while left <= right and nums[left] < pivot:
36                left += 1
37            while left <= right and pivot < nums[right]:
38                right -= 1
39
40            if left <= right:
41                nums[left], nums[right] = nums[right], nums[left]
42                left += 1
43                right -= 1
44
45        
46        nums[start], nums[right] = nums[right], nums[start]
47
48        return right
49