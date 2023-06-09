class  Node:
    def __init__(self):
        self.value=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node()

    def add(self, value):
        if self.head.value==None:
            self.head.value=value

        tmp=Node()
        tmp.value=value

# 1 вариант

        #current_node=self.head
        #while current_node.next is not None:
        #    current_node=current_node.next
        #current_node.next=tmp

# 2 вариант

        tmp.next=self.head
        self.head=tmp
         
    def length(self):
        size=0    
        current_node=self.head
        
        while current_node.next is not None:
            current_node=current_node.next
            size+=1
        return size
    
    def find(self, value):
        if self.head.value is None:
            if self.head.value==value:
                return True
        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
            if current_node.value==value:
                return True
            
        return False
    
    def print(self):
        if self.head.value is None:
            print("Список пуст")

        current_node=self.head
        while current_node.next is not None:
            print(current_node.value, end=" ")
            current_node=current_node.next
            

ll=LinkedList() 
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22))   
ll.print()
ll.add(9)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22)) 
ll.print()
ll.add(7)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22))
ll.print()
ll.add(12)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22)) 
ll.print()
ll.add(5)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22)) 
ll.print()
ll.add(6)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22)) 
ll.print()
ll.add(16)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22)) 
ll.print()
ll.add(1)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22)) 
ll.print()
ll.add(11)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22)) 
ll.print()
ll.add(18)
#print(ll.length())
print(ll.find(0), ll.find(9), ll.find(11), ll.find(22)) 
ll.print()