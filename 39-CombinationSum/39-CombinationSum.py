# Last updated: 5/16/2026, 12:30:35 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()

        self.pathSum = 0
        self.track = []
        self.res = []

        self.dfs(candidates, target, 0)
        return self.res


    def dfs(self, candidates, target, start):

        if self.pathSum == target:
            self.res.append(self.track.copy())
            return

        if self.pathSum > target:
            return

        for i in range(start, len(candidates)):
            val = candidates[i]

            self.track.append(val)
            self.pathSum += val
            self.dfs(candidates, target, i)
            self.pathSum -= val
            self.track.pop()
            


        
