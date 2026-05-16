# Last updated: 5/16/2026, 12:28:21 PM
from heapq import heappush
from collections import Counter
class Solution:
# Method 3 ===========================================================
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        dict_nums = {}
        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1
        
        h = []
        heapq.heapify(h)
        
        i = 0
        for num, freq in dict_nums.items():
            if i < k:
                heapq.heappush(h, (freq, num))
            else:
                heapq.heappushpop(h, (freq, num))
            i += 1

        return [item[1] for item in h]





# Method 2 ===========================================================
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    #     dict_nums = Counter(nums)
    #     return [item[0] for item in dict_nums.most_common(k)]




# Method 1 ============================================================
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
    #     count_dict = {}
    #     for num in nums:
    #         if num not in count_dict:
    #             count_dict[num] = 0
    #         else:
    #             count_dict[num] += 1

    #     h = []
    #     # print(count_dict)

    #     for key, val in count_dict.items():
    #         if k > 0:
    #             heappush(h, (val, key))
    #             k -= 1
    #         else:
                
    #             heappush(h, (val, key))
    #             heappop(h)

    #     # print(len(h))

    #     out = []
    #     for i in range(len(h)):
    #         tmp = heappop(h)
    #         out.append(tmp[1])
    #     return out
            