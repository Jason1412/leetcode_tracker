# Last updated: 5/16/2026, 12:28:36 PM
class MedianFinder:

    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        
        if len(self.large) <= len(self.small):
            tmp = heapq.heappushpop(self.small, -num)
            heapq.heappush(self.large, -tmp)
        else:
            tmp = heapq.heappushpop(self.large, num)
            heapq.heappush(self.small, -tmp)



    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()