

# DSA in Python - Find Pairs with Given Sum in Doubly Linked List | Brute to Optimal | GFG | Part 166


# ------------most optimised solution----------
def sum(head,target):
    if head is None:
            return []
    front = head
    tail = head
    result = []
    while tail.next is not None:
        tail = tail.next
    
    while front != tail and front.prev != tail:
        if front.val+ tail.val == target:
            result.append([front.val , tail.val])
            front =  front.next
            tail = tail.prev
        elif front.val + tail.val > target:
            tail = tail.prev
        else:
            front = front.next
    return result



# --------------batter solution_----------------------
def sum(head,target):
    temp = head
    result = []
    my_set = set()
    while temp is not None:
        rem =  target - temp.val
        if rem in my_set:
            result.append([temp.val , rem])
        my_set.add(temp.val)
        temp = temp.next
    return result



# -----------brute force solution-----------------------
def sum(head ,target):
    temp1 = head
    result = []
    while temp1 is not None:
        temp2 = temp1.next
        while temp2 is not None:
            if temp1.val+ temp2.val == target:
                result.append([temp1.val, temp2.val])
            temp2 = temp2.next
        temp1 = temp1.next
    return result

            
            


