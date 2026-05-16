# Last updated: 5/16/2026, 12:29:23 PM
# Version 2 ==================================================
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.hash = OrderedDict()
        self.capacity = capacity


    def get(self, key):
        if key not in self.hash:
            return -1

        out = self.hash[key]
        self.hash.move_to_end(key, last=True)

        return out


    def put(self, key, value):
        
        if key in self.hash:
            self.hash[key] = value
            self.hash.move_to_end(key, last=True)

        else:
            if len(self.hash) >= self.capacity:
                self.hash.popitem(last=False)
            self.hash[key] = value



# # Version 1 ==================================================
# # Double linked list + hashmap
# class Node:
#     def __init__(self, k, v):
#         self.key = k
#         self.value = v
#         self.next = None
#         self.prev = None


# class LRUCache:

#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.head = Node(-1, -1)
#         self.tail = Node(-1, -1)

#         self.hash = {}
#         self.head.next = self.tail
#         self.tail.prev = self.head


#     def get(self, key: int) -> int:
#         if key not in self.hash:
#             return -1
        
#         self.remove(self.hash[key])
#         self.addLast(self.hash[key])
#         return self.hash[key].value


#     def put(self, key: int, value: int) -> None:
#         if key in self.hash:
#             self.hash[key].value = value
#             self.remove(self.hash[key])
#             self.addLast(self.hash[key])

#         else:
#             if len(self.hash) >= self.capacity:
#                 self.removeFirst()
            
#             node = Node(key, value)
#             self.hash[key] = node
#             self.addLast(node)


#     def remove(self, node):
#         node.prev.next = node.next
#         node.next.prev = node.prev


#     def removeFirst(self):

#         node = self.head.next

#         self.head.next = node.next
#         node.next.prev = self.head

#         self.hash.pop(node.key)
        

#     def addLast(self, node):
#         node.next = self.tail
#         node.prev = self.tail.prev
#         self.tail.prev.next = node # !!!
#         self.tail.prev = node







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)