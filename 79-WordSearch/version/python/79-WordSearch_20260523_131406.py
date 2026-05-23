# Last updated: 5/23/2026, 1:14:06 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        
4        nrow, ncol = len(board), len(board[0])
5
6        self.res = []
7
8        # self.visited = [[False for _ in range(ncol)] for _ in range(nrow)]
9        
10        self.count = 0
11        self.found = False
12        
13        for i in range(nrow):
14            for j in range(ncol):
15                if board[i][j] == word[0]:
16                    self.dfs(i, j, board, word)
17
18                if self.found:
19                    return True
20
21        return False
22
23
24
25
26    def dfs(self, row, col, board, word):
27
28        nrow, ncol = len(board), len(board[0])
29
30
31        if ''.join(self.res) == word: # 检查上一步的情况
32            self.found = True
33            return
34
35        if self.found:
36            return
37
38        if row < 0 or col < 0 or row > nrow - 1 or col > ncol - 1:
39            return
40  
41      
42        if board[row][col] != word[self.count]: # The location of this section is important
43            return
44        
45        self.res.append(board[row][col])
46        self.count += 1
47        temp = board[row][col]
48        board[row][col] = '#'
49
50        self.dfs(row+1, col, board, word)
51        self.dfs(row-1, col, board, word)
52        self.dfs(row, col+1, board, word)
53        self.dfs(row, col-1, board, word)
54
55        board[row][col] = temp
56        self.count -= 1
57        self.res.pop()
58
59
60        
61
62
63
64
65