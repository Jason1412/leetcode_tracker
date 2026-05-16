# Last updated: 5/16/2026, 12:28:13 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        
        self.dummy = ListNode(0, head)

        self.n = 0
        while head:
            head = head.next
            self.n += 1


    def getRandom(self) -> int:
        
        ind = random.randint(1, self.n)

        pointer = self.dummy

        for i in range(ind):
            pointer = pointer.next

        return pointer.val
            

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()