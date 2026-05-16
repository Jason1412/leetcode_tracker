# Last updated: 5/16/2026, 12:30:34 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        self.res = []
        self.track = []
        self.used = [False for _ in range(len(candidates))]

        self.dfs(candidates, 0, 0, target)

        return self.res

        

    def dfs(self, candidates, start, cumSum, target):

        if cumSum == target:
            self.res.append(self.track.copy())
            return

        if cumSum > target:
            return            

        for i in range(start, len(candidates)):
            
            if i > 0 and not self.used[i-1] and candidates[i] == candidates[i-1]:
                continue

            self.track.append(candidates[i])
            cumSum += candidates[i]
            self.used[i] = True

            self.dfs(candidates, i+1, cumSum, target)

            self.used[i] = False
            cumSum -= candidates[i]
            self.track.pop()


