

# DSA in Python Course - Remove Duplicates from a Sorted Doubly Linked List | GFG Practice | Part 167

# ---------optimal solution---------
# def removeDuplicates(self, head):
#         if head is None:
#             return None
#         curr =  head.next
#         while curr is not None:
#             if curr.data == curr.prev.data:
#                 if curr.prev == head:
#                     head = curr
#                     curr.prev = None
#                     curr = curr.next
#                 else:
#                     curr.prev.prev.next = curr
#                     curr.prev = curr.prev.prev
#             else:
#                 curr = curr.next
#         return head


# ---------good solution---------
# def remove(self,head):
#     if head is None:
#         return None
#     temp = head
#     my_set = set()
#     while temp is not None:
#         nxt = temp.next
#         if temp.val  in my_set:
#             if temp.prev:
#                 temp.prev.next = temp.next
#             if temp.next:
#                 temp.next.prev = temp.prev
#         else:    
#             my_set.add(temp.val)
#         temp = nxt
#     return head

