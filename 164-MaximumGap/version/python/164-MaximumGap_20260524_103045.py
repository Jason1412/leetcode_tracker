# Last updated: 5/24/2026, 10:30:45 AM
1class Bucket:
2    def __init__(self):
3        self.used = False
4        self.minval = float('inf')
5        self.maxval = float('-inf')
6
7
8class Solution:
9    def maximumGap(self, nums: List[int]) -> int:
10        
11        if len(nums) < 2:
12            return 0
13
14        minVal = min(nums)
15        maxVal = max(nums)
16        n = len(nums)
17
18        bucket_size = max(1, (maxVal - minVal) // (n - 1))
19        bucketNum = (maxVal - minVal) // bucket_size + 1
20        buckets = [Bucket() for _ in range(bucketNum)]
21
22        for num in nums:
23            ind = (num - minVal) // bucket_size
24            
25            buckets[ind].used = True
26            buckets[ind].minval = min(num, buckets[ind].minval)
27            buckets[ind].maxval = max(num, buckets[ind].maxval)
28
29        
30        maxDiff = float('-inf')
31        preMax = minVal
32        
33        for bucket in buckets:
34            if bucket.used:
35                maxDiff = max(maxDiff, bucket.minval - preMax)
36                preMax = bucket.maxval
37
38        
39
40        return maxDiff