class Node:
    def __init__(self):
        self.value=None
        self.next=None
        self.prev=None

class DoubleLinkedList:
    def __init__(self):
        self.head=Node()

    def insert_to_end(self, value):
        if self.head.value is None:
            self.head.value=value
            return
        
        current_nod=self.head
        while current_nod.next is not None:
            current_nod=current_nod.next

        tmp=Node()
        tmp.value=value
        tmp.prev=current_nod
        current_nod.next=tmp

    def insert_to_start(self, value):
        if self.head.value is None:
            self.head.value=value
            return

        tmp=Node()
        tmp.value=value
        tmp.next=self.head
        self.head.prev=tmp
        self.head=tmp
        
    def insert_after_value(self, after_value, value_to_insert):
        if self.head.value is None:
            raise Exception ("Empty list")
        
        if self.head.value==after_value:
           tmp=Node()
           tmp.value=value_to_insert
           tmp.next=self.head.next
           tmp.prev=self.head
           self.head.next.prev=tmp        
           self.head.next=tmp
           return

        current_node=self.head
        while current_node.next is not None:
            if current_node.value==after_value:
                break
            current_node=current_node.next

        if current_node.next is None:
            if current_node.value != after_value:
                raise Exception ("No such element")
            
        tmp=Node()
        tmp.value=value_to_insert
        tmp.next=current_node.next
        tmp.prev=current_node
        current_node.next.prev=tmp        
        current_node.next=tmp

    def delete_from_end(self):
        if self.head.value is None:
            raise Exception ("Empty list")
        
        if self.head.next is None:
            val=self.head.value
            self.head=Node()
            return val

        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
        
        val=current_node.value
        current_node.prev.next=None
        return val

    def delete_from_start(self):
        if self.head.value is None:
            raise Exception ("Empty list")
        
        if self.head.next is None:
            val=self.head.value
            self.head=Node()
            return val

        current_node=self.head
        while current_node.next is not None:
            current_node=current_node.next
        
        self.head.next.prev=None
        val=self.head.value
        self.head=self.head.next
        return val

dll=DoubleLinkedList() 
dll.insert_to_start(9)
dll.insert_to_end(7)
dll.insert_to_start(6)
dll.insert_after_value(9,8)
print(dll.delete_from_end())
print(dll.delete_from_start())
print(dll.delete_from_start())
print(dll.delete_from_start())