class node:
    def __init__(self , val):
        self.val = val
        self.next = None
    
class singly_linked_list:
    def __init__(self):
        self.head = None
    

    def append(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node



    def traverse(self):
        if not self.head:
            print("List is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val , end=" ")
                curr = curr.next
            print()



    def insert(self ,data, position):
        new_node = node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            prev_node = None
            count = 0
            while curr is not None and position > count:
                prev_node = curr
                curr = curr.next
                count +=1
            if prev_node is None:
                print("Invalid Position")
                return    
            prev_node.next = new_node
            new_node.next = curr 



    def Remove(self,val):
        temp = self.head
        if temp is None:
            print("List is empty")
            return
       
        if temp.val == val:
            self.head = temp.next
            temp.next = None
            del temp
            return
        else:
            found = False
            prev = None
            while temp is not None:
                if temp.val == val:
                     found = True
                     break
                prev = temp
                temp = temp.next
            if found:
                prev.next = temp.next
                temp.next = None
                del temp
            else:
                print("Value not found in the list")

            


sll = singly_linked_list()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.append(50)



temp =  sll.head
stack = []
while temp is not None:
    stack.append(temp.val)
    temp = temp.next

temp =  sll.head
while temp is not None:
    temp.val = stack.pop()
    temp = temp.next
    

sll.traverse()

