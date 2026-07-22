#  Delete All Occurrences of a Key in Doubly Linked List | GFG Practice | Part 165


def removeoccurence(head, target):
    if head is None:
        return None

    temp = head
    prev = None
    new_head = head

    while temp is not None:
        if temp.data == target:
            if prev is not None:
                prev.next = temp.next

            if temp.next is not None:
                temp.next.prev = prev

            if temp == new_head:
                new_head = temp.next
                if new_head is not None:
                    new_head.prev = None

            temp = temp.next
        else:
            prev = temp
            temp = temp.next

    return new_head