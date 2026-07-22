# temp = sll.head
# count = 0
# while temp is not None:
#     count += 1
#     temp = temp.next

# temp = sll.head
# for i in range(count//2):
#     temp = temp.next

# print("Middle element of the linked list is:", temp.val)


# //optimal solution--------
slow =sll.head
fast = sll.head
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

print(slow.val)