# Last updated: 5/19/2026, 10:53:30 PM
1class Solution:
2    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
3        
4        self.num_digit = 0
5        self.res = []
6        self.track = 0
7
8        self.dfs(n, k)
9
10        return self.res
11
12
13    def dfs(self, n, k):
14
15        if self.num_digit == n:
16            self.res.append(self.track)
17            return
18        
19        for i in range(10):
20
21            if self.num_digit == 0 and i == 0:
22                continue
23            
24            if self.num_digit > 0 and abs(i - self.track % 10) != k:
25                continue
26
27            self.num_digit += 1
28            self.track = self.track * 10 + i
29            self.dfs(n, k)
30            self.track = self.track // 10
31            self.num_digit -= 1
32
33
34            
35
36        
37
38
39
40
41