# Last updated: 5/16/2026, 12:30:23 PM
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        posi = 0

        for intv in intervals:


            if intv[1] >= new_start and intv[0] <= new_end:
                
                new_start = min(intv[0], new_start)
                new_end = max(intv[1], new_end) 
                
            if intv[1] < new_start:
                posi +=1
                res.append(intv)
            
            if intv[0] > new_end:
                res.append(intv)

        
        res.insert(posi, [new_start, new_end])
            
            

        return res
