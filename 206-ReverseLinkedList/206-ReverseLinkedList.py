# Last updated: 5/16/2026, 12:28:59 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        prev = None
        cur = head
        nxt = head.next

        while cur is not None:

            cur.next = prev

            prev = cur
            cur = nxt
            
            if nxt is not None:
                nxt = nxt.next

        return prev