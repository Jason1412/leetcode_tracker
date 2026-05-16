# Last updated: 5/16/2026, 12:25:51 PM
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # intervals.sort(key=lambda x: x[0])

        left, right = intervals[0][0], intervals[0][1]

        count = 0

        for i in range(1, len(intervals)):
            intv = intervals[i]

            print("left=", left)
            print("right=", right)
            print("-------------------")

            # if left <= intv[0] and right >= intv[1]:
            #     count += 1
            # elif right >= intv[0] and right <= intv[1]:
            #     print("merging overlaping intervals")
            #     right = intv[1]
            # elif right < intv[0]:
            #     left = intv[0]
            #     right = intv[1]

        
            if left <= intv[0] and right >= intv[1]:
                count += 1
            
            if left <= intv[0] and right >= intv[0] and right <= intv[1]:
                left = intv[0]
                right = intv[1]
            
            if right < intv[0]:
                left = intv[0]
                right = intv[1]

        return len(intervals) - count