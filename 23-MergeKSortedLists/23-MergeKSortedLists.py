# Last updated: 5/16/2026, 12:30:46 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        h = []
        for node in lists:
            if node:
                h.append((node.val, id(node), node))

        heapq.heapify(h)
        dummy = ListNode(-1)
        head = dummy

        while h:
            val, _, node = heapq.heappop(h)

            head.next = node
            head = head.next

            if node.next:
                heapq.heappush(h, (node.next.val, id(node.next), node.next))

            
        return dummy.next


# Version 2 ========================================================
# import heapq

# ListNode.__lt__ = lambda self, other: self.val < other.val

# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if not lists:
#             return None
#         if len(lists) == 1 and not lists[0]:
#             return None

#         h = []
#         # print(len(lists))
#         for node in lists:
#             if node:
#                 h.append(node)
#         # print(h)

#         heapq.heapify(h)
#         dummy = ListNode(-1)
#         head = dummy
#         while h:
#             node = heapq.heappop(h)
#             head.next = node
#             head = head.next
            
#             # if not node:
#             #     print("-----------------")
#             #     print(node)

#             if node.next is not None:
#                 heapq.heappush(h, node.next)
        
#         return dummy.next






    # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if not lists:
    #         return None
        
    #     if len(lists) == 1 and lists[0] is None:
    #         return None

    #     dummy = ListNode(-1)
    #     out_head = dummy
    #     pq = []
    #     for node in lists:
    #         if node:
    #             heapq.heappush(pq, (node.val, node))


    #     while pq:
    #         (min_val, min_node) = heapq.heappop(pq)
    #         out_head.next = min_node
    #         out_head = out_head.next

    #         if min_node.next:
    #             heapq.heappush(pq, (min_node.next.val, min_node.next))

    #     return dummy.next
            

        
