# Last updated: 5/16/2026, 12:27:14 PM
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ind = self.bsearch(arr, 0, len(arr)-1, x)

        print("ind=", ind)
        i, j = ind-1, ind

        res = []


        for _ in range(k):
            if self.isLeftCloser(arr, x, i, j):
                res.append(arr[i])
                i -= 1
            else:
                res.append(arr[j])
                j += 1
        res.sort()
        return res

            
    def isLeftCloser(self, A, target, left, right):

        if left < 0:
            return False
        if right >= len(A):
            return True
        
        if abs(A[left] - target) <= abs(A[right] - target):
            return True
        
    
    def bsearch(self, arr, start, end, target):

        left = start
        right = end

        while (left + 1 < right):

            mid = (left + right) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid
            elif arr[mid] > target:
                right = mid
            

        if arr[left] > target:
            return left
        
        if arr[left] <= target <= arr[right]:
            if abs(arr[left] - target) <= abs(target - arr[right]):
                return left
            else:
                return right
        
        if arr[right] < target:
            return right



    
