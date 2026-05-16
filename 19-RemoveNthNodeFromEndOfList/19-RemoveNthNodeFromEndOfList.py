# Last updated: 5/16/2026, 12:30:49 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        dummy = ListNode(-1)
        dummy.next = head

        p1, p2 = dummy, head

        for _ in range(n):
            if p2 is None:
                return -1
            p2 = p2.next

            
        while p2:

            p1 = p1.next
            p2 = p2.next
        
        p1.next = p1.next.next
        return dummy.next
