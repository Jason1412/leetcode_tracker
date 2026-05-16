# Last updated: 5/16/2026, 12:27:42 PM
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        i, j = click

        # n_mines = self.num_mines(board, i, j)
        # print("n_mines=", n_mines)

        if board[i][j] == "M":
            board[i][j] = "X"

            return board
        
        visited = set()
        self.dfs(board, i, j, visited)
        return board


    def dfs(self, board, i, j, visited):

        # if (i, j) in visited:
        #     return
        if board[i][j] == 'B' or board[i][j].isdigit():
            return
        
        n_mines = self.num_mines(board, i, j)

        if n_mines > 0:
            board[i][j] = str(n_mines)
            return



        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1],
                [-1, -1], [-1, 1], [1, -1], [1, 1]]

        board[i][j] = 'B'
        visited.add((i, j))

        for d in dirs:
            x = i + d[0]
            y = j + d[1]

            if not self.valid(board, x, y):
                continue
            
            self.dfs(board, x, y, visited)
        

        
    def num_mines(self, board, i, j):

        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1],
                [-1, -1], [-1, 1], [1, -1], [1, 1]]
        
        count = 0
        for d in dirs:
            x = i + d[0]
            y = j + d[1]

            if not self.valid(board, x, y):
                continue

            if board[x][y] == 'M':
                count += 1
        
        return count


    def valid(self, board, i, j):
        nrow, ncol = len(board), len(board[0])

        if 0 <= i <= nrow - 1 and 0 <= j <= ncol - 1:
            return True
        return False