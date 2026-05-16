# Last updated: 5/16/2026, 12:30:11 PM
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        n_list = [i + 1 for i in range(n)]
    
        self.res = []
        self.track = []

        self.dfs(n_list, 0, k)

        return self.res
        


    def dfs(self, n_list, start, k):
        
        if len(self.track) == k:
            self.res.append(self.track.copy())

        
        for i in range(start, len(n_list)):

            self.track.append(n_list[i])

            self.dfs(n_list, i+1, k)

            self.track.pop()
