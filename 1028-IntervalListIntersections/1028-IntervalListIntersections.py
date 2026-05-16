# Last updated: 5/16/2026, 12:26:08 PM
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        n1, n2 = len(firstList), len(secondList)

        i, j = 0, 0

        out = []

        while i < n1 and j < n2:

            a1, a2 = firstList[i][0], firstList[i][1]
            b1, b2 = secondList[j][0], secondList[j][1]

            if a1 <= b2 and a2 >= b1:
                out.append([max(a1, b1), min(a2, b2)])

            if a2 < b2:
                i += 1
            else:
                j += 1

        return out
            



