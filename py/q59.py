


# 141. Linked List Cycle

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
sll.append(10)
sll.append(20)
sll.append(30)

# ------brute force approach---------
# def check():
#     curr = sll.head
#     mySet = set()
#     while curr is not None:
#         if curr in mySet:
#             return True
#         mySet.add(curr)
#         curr = curr.next
#     return False

# print(check())


# ------optimal approach---------
def check():
    slow = sll.head
    fast = sll.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
        





            
                
                    

                

    

    


    
            
         
         
      
      