# Last updated: 5/25/2026, 2:19:57 PM
1class Solution:
2    def sortArray(self, nums: List[int]) -> List[int]:
3        
4        self.tmp = [0 for _ in range(len(nums))]
5        
6        self.mergeSort(nums, 0, len(nums)-1)
7
8        return nums
9
10        
11
12    def mergeSort(self, nums, start, end):
13
14        if start >= end:
15            return
16
17        mid = start + (end - start) // 2
18
19        self.mergeSort(nums, start, mid)
20        self.mergeSort(nums, mid+1, end)
21
22        self.merge(nums, start, mid, end)
23
24
25    def merge(self, nums, start, mid, end):
26
27        left = start
28        right = mid + 1
29
30        ind_tmp = start
31
32        while left <= mid and right <= end:
33            if nums[left] < nums[right]:
34                self.tmp[ind_tmp] = nums[left]
35                left += 1
36                ind_tmp += 1
37            else:
38                self.tmp[ind_tmp] = nums[right]
39                right += 1
40                ind_tmp += 1
41
42        while left <= mid:
43            self.tmp[ind_tmp] = nums[left]
44            ind_tmp += 1
45            left += 1
46
47        while right <= end:
48            self.tmp[ind_tmp] = nums[right]
49            ind_tmp += 1
50            right += 1
51
52        for i in range(start, end+1):
53            nums[i] = self.tmp[i]