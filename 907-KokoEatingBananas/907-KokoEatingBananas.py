# Last updated: 5/16/2026, 12:26:32 PM
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = 1_000_000_000

        while left + 1 < right:
            mid = left + (right - left) // 2
            
            if self.find_time(piles, mid) < h:
                right = mid
            elif self.find_time(piles, mid) > h:
                left = mid
            elif self.find_time(piles, mid) == h:
                right = mid

        if self.find_time(piles, left) <= h:
            return left
        elif self.find_time(piles, right) <= h:
            return right
        



    def find_time(self, piles, x) -> int:
        hours = 0
        for pile in piles:
            hours += pile // x
            if pile % x > 0:
                hours += 1
            
        return hours