# Last updated: 5/16/2026, 12:26:14 PM
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        self.res = []
        start = 0
        end = len(arr) - 1

        for i in range(end, -1, -1):
            self.helper(arr, start, i)

        return self.res

    
    def helper(self, arr, start, end):

        if start >= end:
            return

        ind_max = start
        max_val = arr[start]
        for i in range(start, end+1):
            if arr[i] > max_val:
                max_val = arr[i]
                ind_max = i
        
        if ind_max == end:
            return

        self.res.append(ind_max + 1)

        self.reverse(arr, start, ind_max)

        self.res.append(end + 1)
        self.reverse(arr, 0, end)
        
    def reverse(self, arr, start, end):

        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
