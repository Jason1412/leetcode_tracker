# Last updated: 5/16/2026, 12:27:02 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        n = len(temperatures)

        s = []
        t = temperatures

        res = [0 for _ in range(n)]

        for i in range(n-1, -1, -1):

            while s and t[i] >= t[s[-1]]:
                s.pop()

            if s:
                res[i] = s[-1] - i
            
            s.append(i)


        return res