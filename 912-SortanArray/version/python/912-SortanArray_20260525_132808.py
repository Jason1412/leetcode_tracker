# Last updated: 5/25/2026, 1:28:08 PM
1import random
2class Solution:
3    def sortArray(self, nums: List[int]) -> List[int]:
4        
5        random.shuffle(nums)
6        self.quickSort(nums, 0, len(nums)-1)
7
8        return nums
9
10
11    def partition(self, nums, low, high):
12
13        left = low + 1
14        right = high
15
16        pivot = nums[low]
17
18        while left <= right:
19            while left <= right and nums[left] < pivot:
20                left += 1
21
22            while left <= right and pivot < nums[right]:
23                right -= 1
24
25            if left <= right:
26                nums[left], nums[right] = nums[right], nums[left]
27                left += 1
28                right -= 1
29
30        nums[low], nums[right] = nums[right], nums[low]
31
32        return right
33
34
35    def quickSort(self, nums, low, high):
36        if len(nums) == 0:
37            return
38        if low >= high:
39            return
40        
41        p = self.partition(nums, low, high)
42
43
44        self.quickSort(nums, low, p-1)
45        self.quickSort(nums, p+1, high)
46
47
48
49    