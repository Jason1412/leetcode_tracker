# Last updated: 5/24/2026, 7:17:02 PM
1class Solution:
2    def gameOfLife(self, board: List[List[int]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        
6        Rules:
7        Live cell
8            < 2 live neighbors, dies    1 -> -1
9            2 <= x <= 3 live neighbors, lives on
10            > 3 live neighbors, dies    1 -> -1
11        Dead cell
12            = 3 live neighbors, lives   0 -> 2
13        """
14        
15        dirs = [(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
16
17        nrow, ncol = len(board), len(board[0])
18
19        for i in range(nrow):
20            for j in range(ncol):
21
22                num_live = 0
23
24                for d in dirs:
25                    new_i = i + d[0]
26                    new_j = j + d[1]
27
28                    if new_i < 0 or new_j < 0 or new_i > nrow - 1 or new_j > ncol - 1:
29                        continue
30
31                    if abs(board[new_i][new_j]) == 1:
32                        num_live += 1
33
34                if board[i][j] == 1 and (num_live < 2 or num_live > 3):
35                    board[i][j] = -1
36
37                if board[i][j] == 0 and num_live == 3:
38                    board[i][j] = 2
39
40
41        for i in range(nrow):
42            for j in range(ncol):
43                if board[i][j] == -1:
44                    board[i][j] = 0
45                if board[i][j] == 2:
46                    board[i][j] = 1
47
48        
49        
50    
51
52        