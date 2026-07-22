# Doubly Linked List Methods Explained with Code | Insert, Delete, Traverse | Part 163


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def append(self,data):
        new_node =Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
    def insert_at_index(self,pos,data):
        new_node = Node(data)
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.insert_at_head(data)
            return
        curr = self.head
        ind = 0
        while ind < pos-1 and curr :
            curr = curr.next
            ind += 1
       
        if curr is None:
            print("position is out of bound")
            return
        
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev=  new_node
        curr.next = new_node

        if new_node.next is None:
            self.tail = new_node

    def traverse(self):
        curr = self.head
        while curr is not None:
            print(curr.data ,end="<->")
            curr = curr.next
        print(None)
    
    def reverse(self):
        curr = self.tail
        while curr is not None:
            print(curr.data , end="<->")
            curr = curr.prev
        print(None)

    def delete_head(self):
        if not self.head:
            print("empty list")
            return
            
        if self.head.next is None:
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next
        self.head.prev = None

    def delete_tail(self):
        if self.tail is None:
            print("List is empty")
            return
        if self.tail.prev is None:
            self.tail = None
            self.head = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

    def delete_indx(self,pos):
        if pos < 0:
            print("Invalid position")
            return
        if pos == 0:
            self.delete_head()
            return
        
        curr = self.head
        idx = 0
        while idx < pos and curr:
            curr= curr.next
            idx +=1

        if curr is None:
            print("out of bound poss")
            return
            
        if curr.next is None:
            self.delete_tail()
            return
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
            

        
ddl = DoublyLinkedList()
ddl.insert_at_head(10)

ddl.append(20)
ddl.append(30)
ddl.append(40)
ddl.append(50)

ddl.traverse()
ddl.reverse()

ddl.insert_at_index(2,25)
ddl.traverse()
ddl.delete_head()
ddl.delete_tail()
ddl.traverse()
ddl.delete_indx(2)
ddl.traverse()




        