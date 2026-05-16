# Last updated: 5/16/2026, 12:27:13 PM
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        freq = {}
        need = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        
        for num in nums:
            if freq[num] == 0:
                continue

            if num in need and need[num] > 0:
                freq[num] -= 1
                need[num] -= 1

                need[num+1] = need.get(num+1, 0) + 1

            elif freq[num] > 0 and freq.get(num+1, 0) > 0 and freq.get(num+2, 0) > 0: # Here, freq[num] may be 0. Thus, we need to skip the cases when freq[num] == 0 in the beginning of the for loop.
                freq[num] -= 1
                freq[num+1] -= 1
                freq[num+2] -= 1
                need[num+3] = need.get(num+3, 0) + 1
            else:
                return False

        return True
            