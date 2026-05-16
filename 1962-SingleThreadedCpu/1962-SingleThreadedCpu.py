# Last updated: 5/16/2026, 12:25:26 PM
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)

        triples = []
        for i in range(n):
            triples.append([tasks[i][0], tasks[i][1], i])

        triples.sort(key=lambda x: x[0])

        pq = []
        res = []

        now = 0
        i = 0
        while len(res) < n:
            
            while i < n and triples[i][0] <= now:
                heapq.heappush(pq, (triples[i][1], triples[i][2]))
                i += 1
        
            if pq:
                processing_time, original_index = heapq.heappop(pq)
                res.append(original_index)
                now += processing_time
            elif i < n and triples[i][0] > now:
                now = triples[i][0]


        return res