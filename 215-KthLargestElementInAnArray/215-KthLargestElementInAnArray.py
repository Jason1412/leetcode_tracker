# Last updated: 5/16/2026, 12:28:56 PM
import heapq as hq
class Solution:
    # def findKthLargest(self, nums: List[int], k: int) -> int:
    #     k = len(nums) - k
    #     self.shuffle(nums)
    #     return self.quickSort(nums, 0, len(nums)-1, k)


    # def shuffle(self, nums):
    #     n = len(nums)
    #     for i in range(n):
    #         r = i + random.randint(0, n-i-1)
    #         nums[i], nums[r] = nums[r], nums[i]


    # def quickSort(self, nums, start, end, k):

    #     while (start <= end):
    #         ind_p = self.partition(nums, start, end)

    #         if ind_p == k:
    #             return nums[k]
    #         elif ind_p < k:
    #             start = ind_p + 1
    #         elif ind_p > k:
    #             end = ind_p - 1

    #     return -1



    # def partition(self, nums, start, end):
    #     left = start + 1
    #     right = end

    #     pivot = nums[start]

    #     while (left <= right):
    #         while (left <= right and nums[left] < pivot):
    #             left += 1
    #         while (left <= right and nums[right] > pivot):
    #             right -= 1

    #         if (left <= right):
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right -= 1

    #     nums[start], nums[right] = nums[right], nums[start]
        
    #     return right

    




# Method 1 --------------------------------------------------------

    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        pq = [num for num in nums[0:k]]
        hq.heapify(pq)


        top_pq = hq.heappop(pq)
        for i in range(k, len(nums)):
            
            if nums[i] >= top_pq:
                hq.heappush(pq, nums[i])
                top_pq = hq.heappop(pq)
        return top_pq

