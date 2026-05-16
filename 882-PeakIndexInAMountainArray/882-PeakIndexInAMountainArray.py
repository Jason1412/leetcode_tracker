# Last updated: 5/16/2026, 12:26:38 PM
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.find_peak(arr)


    def find_peak(self, arr):
        
        start = 1
        end = len(arr) - 2

        while (start + 1 < end):
            mid = (start + end) // 2

            if self.check_shape(arr, mid) == 0:
                return mid
            elif self.check_shape(arr, mid) == 1:
                start = mid
            elif self.check_shape(arr, mid) == -1:
                end = mid

        if self.check_shape(arr, start) == 0:
            return start
        else:
            return end

    
    def check_shape(self, arr, ind):
        
        if arr[ind-1] < arr[ind] and arr[ind] > arr[ind+1]:
            return 0
        
        elif arr[ind-1] > arr[ind]:
            return -1

        elif arr[ind] < arr[ind+1]:
            return 1