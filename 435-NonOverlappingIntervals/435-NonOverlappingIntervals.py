# Last updated: 5/16/2026, 12:28:04 PM
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return None

        n = len(intervals)
        return n - self.maxNonoverlap(intervals)



    def maxNonoverlap(self, intervals):
        intervals.sort(key=lambda x: x[1])
        
        count = 1
        x_end = intervals[0][1]

        for intval in intervals:
            
            if intval[0] >= x_end:
                count += 1
                x_end = intval[1]

        return count