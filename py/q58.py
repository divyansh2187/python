
# -------------optimised------------------

# def reverseList(self, head):
#         temp = head
#         prev = None
#         while temp is not None:
#             front = temp.next
#             temp.next = prev
#             prev = temp
#             temp = front
#         return prev





# --------brute force ----------

# temp =  sll.head
# stack = []
# while temp is not None:
#     stack.append(temp.val)
#     temp = temp.next

# temp =  sll.head
# while temp is not None:
#     temp.val = stack.pop