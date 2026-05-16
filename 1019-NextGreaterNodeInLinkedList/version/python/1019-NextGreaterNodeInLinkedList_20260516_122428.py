# Last updated: 5/16/2026, 12:24:28 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
8        
9        nums = []
10        p = head
11
12        while p is not None:
13            nums.append(p.val)
14            p = p.next
15
16        
17        answer = [0] * len(nums)
18        n = len(nums)
19        stack = []
20        for i in range(n-1, -1, -1):
21            
22            while stack and nums[stack[-1]] <= nums[i]:
23                stack.pop()
24
25            if not stack:
26                answer[i] = 0
27            else:
28                answer[i] = nums[stack[-1]]
29
30            stack.append(i)
31            
32        return answer