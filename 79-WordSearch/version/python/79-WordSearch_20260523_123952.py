# Last updated: 5/23/2026, 12:39:52 PM
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
30        if ''.join(self.res) == word:
31            self.found = True
32            return
33
34        if self.found:
35            return
36
37        if row < 0 or col < 0 or row > nrow - 1 or col > ncol - 1:
38            return
39  
40      
41        if board[row][col] != word[self.count]: # The location of this section is important
42            return
43        
44        self.res.append(board[row][col])
45        self.count += 1
46        temp = board[row][col]
47        board[row][col] = '#'
48
49        self.dfs(row+1, col, board, word)
50        self.dfs(row-1, col, board, word)
51        self.dfs(row, col+1, board, word)
52        self.dfs(row, col-1, board, word)
53
54        board[row][col] = temp
55        self.count -= 1
56        self.res.pop()
57
58
59        
60
61
62
63
64