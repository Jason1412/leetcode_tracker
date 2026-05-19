# Last updated: 5/18/2026, 10:21:31 PM
1class Solution:
2    def combine(self, n: int, k: int) -> List[List[int]]:
3        
4        self.res = []
5        self.track = []
6
7        self.backtrack(1, n, k)
8
9        return self.res
10
11
12    def backtrack(self, start: int, n: int, k: int) -> None:
13
14
15
16        if len(self.track) == k:
17            self.res.append(self.track.copy())
18            
19
20
21        for i in range(start, n+1):
22
23            self.track.append(i)
24            self.backtrack(i+1, n, k)
25            self.track.pop()