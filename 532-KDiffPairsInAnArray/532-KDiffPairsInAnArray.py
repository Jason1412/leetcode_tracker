# Last updated: 5/16/2026, 12:27:40 PM
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        out = set()
        for num in nums:
            
            if k != 0:
                if num + k in seen:
                    out.add(frozenset([num+k, num]))
                if num - k in seen:
                    out.add(frozenset([num-k, num]))
            else:
                if num in seen:
                    out.add(frozenset([num, num]))
                    
            if num not in seen:
                seen.add(num)
        return len(out)