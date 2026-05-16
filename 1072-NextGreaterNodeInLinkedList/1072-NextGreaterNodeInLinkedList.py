# Last updated: 5/16/2026, 12:26:01 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        nums = []
        p = head

        while p is not None:
            nums.append(p.val)
            p = p.next

        
        answer = [0] * len(nums)
        n = len(nums)
        stack = []
        for i in range(n-1, -1, -1):
            
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            if not stack:
                answer[i] = 0
            else:
                answer[i] = nums[stack[-1]]

            stack.append(i)
            
        return answer