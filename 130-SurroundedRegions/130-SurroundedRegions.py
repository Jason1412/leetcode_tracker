# Last updated: 5/16/2026, 12:29:32 PM
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        m = len(board)
        n = len(board[0])

        # Steps:
        # 1. Find the O on the 4 edges. Connect those to dummy
        # 2. Find the possible inner O, which is connected to the O on the edge
        # 3. Fill in the inner Os by Xs

        uf = UF(m * n + 1)
        
        for i in range(m):
            # 1st column
            if board[i][0] == 'O':
                uf.union(i * n + 0, m * n)
            if board[i][n-1] == 'O':
                uf.union(i * n + n - 1, m * n)
        
        for j in range(n):
            if board[0][j] == 'O':
                uf.union(j, m * n)
            if board[m-1][j] == 'O':
                uf.union((m - 1) * n + j, m * n)


        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    for move in moves:
                        x = i + move[0]
                        y = j + move[1]
                        if board[x][y] == 'O':
                            uf.union(i * n + j, x * n + y)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not uf.connected(i * n + j, m * n):
                    board[i][j] = 'X'
        


             





class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [-1 for _ in range(n)]

        for i in range(n):
            self.parent[i] = i


    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return
        
        self.parent[root_q] = root_p
        self.count -= 1


    def connected(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        return root_p == root_q


    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]