
# Reverse a Doubly Linked List | GFG Practice | Part 164

# -----------optimal solution--------------------
def reverse_linked_list(head):
    curr = head
    prev = None
    while curr is not None:
        front = curr.next
        curr.prev , curr.next = curr.next , curr.prev
        prev = curr
        curr = front

    return prev


# ----------brute force solution---------
def reverse_linked_list(head):
    curr = head
    stack = []
    while curr is not None:
        stack.append(curr.data)
        curr = curr.next
    curr = head
    while curr is not None:
        curr.data = stack.pop()
        curr = curr.next





        
    