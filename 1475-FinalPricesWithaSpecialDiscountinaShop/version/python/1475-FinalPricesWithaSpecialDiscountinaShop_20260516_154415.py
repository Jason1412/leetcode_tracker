# Last updated: 5/16/2026, 3:44:15 PM
1class Solution:
2    def finalPrices(self, prices: List[int]) -> List[int]:
3        
4
5        indices = self.nextLarge(prices)
6        n = len(prices)
7        out = [0] * n
8
9        for i in range(n):
10            if indices[i] == -1:
11                out[i] = prices[i]
12            else:
13                out[i] = prices[i] - prices[indices[i]]
14            
15        return out
16
17    
18    def nextLarge(self, nums):
19
20        n = len(nums)
21
22        res = [0] * n
23        stack = []
24
25        for i in range(n-1, -1, -1):
26
27            while stack and nums[i] < nums[stack[-1]]:
28                stack.pop()
29
30            if not stack:
31                res[i] = -1
32            else:
33                res[i] = stack[-1]
34
35            stack.append(i)
36
37        return res
38
39