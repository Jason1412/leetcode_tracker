# Last updated: 5/16/2026, 12:30:09 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.flag = False
        self.path = []
        self.path_ind = 0
        self.visited = set()

        nrow, ncol = len(board), len(board[0])

        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    self.dfs(board, word, i, j)

                if self.flag:
                    return True

        return self.flag


    def dfs(self, board, word, i, j):

        if self.flag is True or not self.valid(board, i, j) or (i,j) in self.visited or self.path_ind >= len(word) or board[i][j] != word[self.path_ind]:
            return

        
        self.path.append(word[self.path_ind])
        self.visited.add((i,j))
 
        if self.path_ind == len(word)-1:
            self.flag = True
            return

        self.path_ind += 1 # 如果之前没有return的话, 可能某一次recursion会
        # out of range. 

        self.dfs(board, word, i+1, j)
        self.dfs(board, word, i-1, j)
        self.dfs(board, word, i, j+1)
        self.dfs(board, word, i, j-1)

        self.path_ind -= 1
        self.path.pop()
        self.visited.remove((i,j))

        

    def valid(self, board, i, j):
        nrow, ncol = len(board), len(board[0])

        if 0 <= i <= nrow-1 and 0 <= j <= ncol-1:
            return True
        return False

