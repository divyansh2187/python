# 142. Linked List Cycle II
# -----------brute force -----------


def starting(self , head):
    curr = head
    mySet = set()
    while curr is not None:
        if curr in mySet:
            return curr
        mySet.add(curr)
        curr = curr.next
    return None


# ---------optimal solution ------------

def detectCycle(self, head):
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast =  fast.next
                return fast
        return None 
        


