# Last updated: 5/16/2026, 12:29:28 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return

        dummy = Node(-1)
        dummy_c = Node(-1)

        dummy.next = head

        mappings = {}

        while head:
            mappings[head] = Node(head.val)
            head = head.next


        head = dummy.next
        dummy_c.next = mappings[head]
        print(mappings)

        while head:
            if head.next:
                mappings[head].next = mappings[head.next]
            if head.random:
                mappings[head].random = mappings[head.random]
            # if head.next:
            #     mappings[head].next = mappings[head.next]
            # if head.random:
            #     mappings[head].random = mappings[head.random]
            head = head.next
        
        return dummy_c.next
        



















    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
    #     # print(head)
    #     # print(head.next.random)
    #     if not head:
    #         return None

    #     OrigToCopy = {}

    #     dummy = Node(-1)
    #     dummy.next = head


    #     while head:
    #         OrigToCopy[head] = Node(head.val)
    #         head = head.next
        
    #     head = dummy.next
    #     dummy_c = Node(-1)
    #     dummy_c.next = OrigToCopy[head]

    #     while head:
    #         node_copy = OrigToCopy[head]

    #         if head.random:
    #             node_copy.random = OrigToCopy[head.random]
    #         else:
    #             node_copy.random = None
            
    #         if head.next:
    #             node_copy.next = OrigToCopy[head.next]
    #         else:
    #             node_copy.next = None

    #         head = head.next
        
    #     return dummy_c.next


        # nodes = set()

        # dummy_c = Node(-1)
        # dummy = Node(-1)
        
        # dummy.next = head
        # head_c = dummy_c

        # while head:
        #     head_c.next = Node(head.val)
        #     nodes.add(head_c.next)

        #     if head.random not in nodes:



# Q: Can we put node in set()?
# Q: 

    # In this version, I assumed random is the index, seems it should be the node
    # def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
    #     node_map = {}
    #     node_map_c = {}

    #     dummy_c = Node(-1)
    #     dummy = Node(-1)
    #     dummy.next = head

    #     i = 0
    #     head_copy = dummy_c
    #     while head:
    #         head_copy.next = Node(head.val)
    #         node_map_c[i] = head_copy.next
    #         node_map[i] = head

    #         head_copy = head_copy.next
    #         head = head.next
    #         i += 1

    #     head_copy.next = None

    #     for i in node_map.keys():
    #         rand_ind = node_map[i].random
    #         if rand_ind:
    #             print(rand_ind)
    #             node_map_c[i].random = node_map_c[rand_ind]
    #         else:
    #             node_map_c[i].random = None
    #     return dummy_c.next


        