# Leetcode 328: Odd Even Linked List | Rearrange Nodes | Part 62 


class node:
   def __init__(self,val):
      self.val = val
      self.next = None

class singleLinkList:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = node(data)
        if self.head is None:
           self.head = new_node
        else:
           curr = self.head
           while curr.next is not None:
               curr = curr.next
           curr.next = new_node

    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val , end=" ")
                curr = curr.next
            print()

    def insert(self,data,pos):
        new_node  = node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev = None
            count = 0
            while curr is not None and pos > count:
                prev = curr
                curr = curr.next
                count+=1
            if prev is None:
                print("INVALID index")
                return
            if count != pos:
                print("Invalid Position")
                return
            prev.next = new_node
            new_node.next = curr

    def remove(self ,val):
        curr = self.head
        if curr is None:
            print("list is empty")
            return
        if curr.val == val:
            self.head = curr.next
            curr.next = None
            del curr
            return
        else:
            prev = None
            found  =  False
            while curr is not None:
                if curr.val == val:
                    found = True
                    break
                prev = curr
                curr = curr.next
            if found:
                prev.next = curr.next
                curr.next = None
                del curr
            else:
                print("Value not found in the list")


sll = singleLinkList()
sll.append(8)
sll.append(7)
sll.append(1)
sll.append(5)
sll.append(6)
sll.append(4)


# --------------optimised approach----------------
def oDDeven(self):
    odd = self.head
    even = self.head.next
    pointer = self.head.next
    while even is not None and even.next is not None:
        odd.next = odd.next.next
        odd = odd.next
        even.next = even.next.next
        even = even.next

    odd.next = pointer

    return self.head






# -------------brute force approach----------------
# def oDDeven(self):
#     arr = []
#     odd = self.head
#     indx = self.head
#     even = self.head.next
#     while odd is not None:
#         arr.append(odd.val)
#         odd = odd.next.next if odd.next else None
#     while even is not None:
#         arr.append(even.val)
#         even = even.next.next if even.next else None
#     while indx is not None:
#         indx.val = arr.pop(0)
#         indx = indx.next
    
#     return self.head

oDDeven(sll)
sll.traverse()

    
