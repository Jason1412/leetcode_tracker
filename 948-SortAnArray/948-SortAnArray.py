# Last updated: 5/16/2026, 12:26:26 PM
import random
class Solution:
# Method 2: Quick Sort v2 ------------------------------------------
    # def sortArray(self, nums: List[int]) -> List[int]:

    #     self.shuffle(nums)
    #     self.quickSort(nums, 0, len(nums)-1)
    #     return nums

    # def shuffle(self, nums):
    #     n = len(nums)
    #     for i in range(n):
    #         r = i + random.randint(0, n-i-1)
    #         nums[i], nums[r] = nums[r], nums[i]

    # def quickSort(self, nums, start, end):
        
    #     if start >= end:
    #         return 
        
    #     p = self.partition(nums, start, end)
        
    #     self.quickSort(nums, start, p-1)
    #     self.quickSort(nums, p+1, end)


    # def partition(self, nums, start, end):
    #     left = start
    #     right = end-1

    #     pivot = nums[end]

    #     while (left <= right):
    #         while (left <= right and nums[left] < pivot):
    #             left += 1
    #         while (left <= right and nums[right] > pivot):
    #             right -= 1
            
    #         if (left <= right):
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1
            
        
    #     # At this step, nums[right] <= pivot
    #     # right 最左可以在start的位置
    #     # swap nums[start], nums[right]
    #     print("left, right ={} {}".format(left, right))

    #     nums[end], nums[left] = nums[left], nums[end]

    #     return left
        




# Method 2: Quick Sort -------------------------------------------
    # def sortArray(self, nums: List[int]) -> List[int]:

    #     self.quickSort(nums, 0, len(nums)-1)
    #     return nums

    # def quickSort(self, nums, start, end):
        
    #     if start >= end:
    #         return

    #     mid = random.randint(start, end)
    #     # mid = (start + end) // 2
    #     pivot = nums[mid]

    #     left = start
    #     right = end

    #     while (left <= right):
    #         while (left <= right and nums[left] < pivot):
    #             left += 1
    #         while (left <= right and nums[right] > pivot):
    #             right -= 1
            
    #         if (left <= right):
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1

        
    #     self.quickSort(nums, start, right)
    #     self.quickSort(nums, left, end)











# # Method 1: Merge Sort ----------------------------------------
#     def sortArray(self, nums: List[int]) -> List[int]:
        
#         tmp = [0 for _ in range(len(nums))]
#         self.mergeSort(nums, 0, len(nums)-1, tmp)
#         print("main function:")
#         print("nums =", nums)
#         print("tmp =", tmp)
        
#         # return tmp
#         return tmp



#     def mergeSort(self, nums, start, end, tmp):
        
#         if start >= end:
#             return

#         mid = (start + end) // 2

#         self.mergeSort(nums, start, mid, tmp)
#         self.mergeSort(nums, mid+1, end, tmp)

#         # start, end之间有至少2个element
#         self.merge(nums, start, mid, end, tmp)
#         print('After merge ----------------------------')
#         print('nums=', nums)
#         print('tmp=', tmp)



#     def merge(self, nums, start, mid, end, tmp):
        
#         left = start
#         right = mid + 1
#         index = start

#         print('Before merge ----------------------------')
#         print('nums=', nums)
#         print('tmp=', tmp)


#         while (left <= mid and right <= end):
#             if nums[left] < nums[right]:
#                 tmp[index] = nums[left]
#                 index += 1
#                 left += 1
#             else:
#                 tmp[index] = nums[right]
#                 index += 1
#                 right += 1
        
#         while (left <= mid):
#             tmp[index] = nums[left]
#             index += 1
#             left += 1

#         while (right <= end):
#             tmp[index] = nums[right]
#             index += 1
#             right += 1
        
#         for index in range(start, end+1):
#             nums[index] = tmp[index]



    def sortArray(self, nums: List[int]) -> List[int]:
        
        self.shuffle(nums)

        self.quickSort(nums, 0, len(nums)-1)

        return nums

    def shuffle(self, nums):
        n = len(nums)
        for i in range(n):
            r = i + random.randint(0, n-i-1)
            nums[i], nums[r] = nums[r], nums[i]


    def quickSort(self, nums, start, end):

        if start >= end:
            return

        p = self.partition(nums, start, end)

        self.quickSort(nums, start, p-1)
        self.quickSort(nums, p+1, end)


    def partition(self, nums, start, end):

        pivot = nums[start]
        left = start + 1
        right = end

        while (left <= right):
            while (left <= right and nums[left] < pivot):
                left += 1
            while (left <= right and nums[right] > pivot):
                right -= 1
            
            if (left <= right):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        nums[start], nums[right] = nums[right], nums[start]

        return right