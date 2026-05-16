# Last updated: 5/16/2026, 12:28:28 PM
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        
        arr = []
        
        for i, num in enumerate(nums):
            arr.append(Pair(num, i))

        self.count = [0 for _ in range(len(nums))]

        tmp = [0 for _ in range(len(nums))]

        self.mergeSort(arr, 0, len(nums)-1, tmp)


        # return [self.dict_count[num] for num in orig_nums]
        return self.count

    def mergeSort(self, nums, start, end, tmp):
        
        if start >= end:
            return

        mid = (start + end) // 2

        self.mergeSort(nums, start, mid, tmp)
        self.mergeSort(nums, mid + 1, end, tmp)
        self.merge(nums, start, mid, end, tmp)
        

    def merge(self, nums, start, mid, end, tmp):
        
        left = start
        right = mid + 1
        index = start

        while (left <= mid and right <= end):
            if nums[left].val <= nums[right].val:
                tmp[index] = nums[left]
                self.count[nums[left].pos] += right - mid - 1
                left += 1
                
            else:
                tmp[index] = nums[right]
                right += 1

            index += 1

        while (left <= mid):
            tmp[index] = nums[left]
            self.count[nums[left].pos] += right - mid - 1
            left += 1
            index += 1
        
        while (right <= end):
            tmp[index] = nums[right]
            right += 1
            index += 1

        for index in range(start, end+1):
            nums[index] = tmp[index]
            

class Pair:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
