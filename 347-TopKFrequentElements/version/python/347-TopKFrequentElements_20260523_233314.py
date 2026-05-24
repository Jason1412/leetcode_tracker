# Last updated: 5/23/2026, 11:33:14 PM
1
2import heapq
3from collections import Counter
4
5class Solution:
6    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
7        val_to_freq = Counter(nums)        
8
9        pq = []
10        for val, freq in val_to_freq.items():
11            heapq.heappush(pq, (freq, val))
12            
13            if len(pq) > k:
14                heapq.heappop(pq)
15
16        res = []
17        for i in range(k):
18            res.append(heapq.heappop(pq)[1])
19
20        return res[::-1]