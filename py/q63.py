#  Leetcode 19: Remove Nth Node from End of List | Two Pointer Approach
def remove(self,idx):
    fast =  self.head
    slow = self.head
    for _ in range(idx):
        fast = fast.next
        
    if fast is None:
       self.head = self.head.next
       return
    
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next



# --------brute force solution---------
def remove(self,indx):
    curr = self.head
    len = 0
    while curr is not None:
        len +=1
        curr = curr.next
    if indx == len - 1:
        self.head = self.head.next
        return
    target = len-indx-2
    len = 0
    curr = self.head
    while len < target :
        len +=1
        curr = curr.next

    curr.next = curr.next.next








