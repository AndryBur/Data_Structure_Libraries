class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.value=None
        self.parent=None

class BinarySearchTree:
    def __init__(self):
        self.root=Node()

#  заполнению дерева из отсортированного списка
    def add_sort_list(self, list):
        mid=len(list)//2
        self.root.value=list[mid]
        cn=self.root
        for i in list[mid-1::-1]:
            cn.left=Node()
            cn.left.value=i
            cn.left.parent=cn
            cn=cn.left
        cn=self.root
        for i in list[mid+1:len(list)]:
            cn.right=Node()
            cn.right.value=i
            cn.right.parent=cn
            cn=cn.right

    def add(self, value):
        if self.root.value is None:
            self.root.value=value
            return
        self.add_date(self.root, value)

    def add_date(self, cn, value):
        if cn.value>value:
            if cn.left is None:
                cn.left=Node()
                cn.left.value=value
                cn.left.parent=cn
            else:
                self.add_date(cn.left, value)
        else:
            if cn.right is None:
                cn.right=Node()
                cn.right.value=value
                cn.right.parent=cn
            else:
                self.add_date(cn.right, value)

    def find(self, value):
        if self.root.value is None:
            return False
        if self.root.value==value:
            return True
        node=self.find_node(self.root, value)
        if node is None:
            return False
        return True
        
    def find_node(self, cn, value):
        if cn is None:
            return None
        if cn.value==value:
            return cn
        if cn.value>value:
            res=self.find_node(cn.left, value)
            return res
        else:
            res=self.find_node(cn.right, value)
            return res
        
    def find_min(self):
        node=self.find_min_node(self.root)
        return node.value

    def find_min_node(self, cn):
        if cn.left is None:
            return cn
        node=self.find_min_node(cn.left)
        return node
    
    def find_max(self):
        node=self.find_max_node(self.root)
        return node.value

    def find_max_node(self, cn):
        if cn.right is None:
            return cn
        node=self.find_max_node(cn.right)
        return node
    
    def delete(self, value):
        if (self.root.left is None) and (self.root.right is None) and (self.root.value==value):
            self.root.value=None
            return
        elif (self.root.left is not None) and (self.root.right is None) and (self.root.value==value):
            self.root=self.root.left
            self.root.parent=None  
            return
        elif (self.root.left is None) and (self.root.right is not None) and (self.root.value==value):
            self.root=self.root.right
            self.root.parent=None  
            return 
        node=self.find_node(self.root, value)
        if node is None:
            raise Exception("Нет узла для удаления")
        self.delete_date(node)

    def delete_date(self, node):

# если нет детей        
        if (node.left is None) and (node.right is None):
            if node.parent.left==node:
                node.parent.left=None
            else:
                node.parent.right=None
            return

# если есть 1 ребенок
        if (node.left is not None) and (node.right is None):
            if node.parent.left==node:
                node.parent.left=node.left
            else:
                node.parent.right=node.left
            return
        
        if (node.left is None) and (node.right is not None):
            if node.parent.left==node:
                node.parent.left=node.right
            else:
                node.parent.right=node.right
            return

# если узел - корень с двумя детьми
        if node==self.root:
           min_node_of_right=self.find_min_node(node.right)
           self.root.value=min_node_of_right.value
           if min_node_of_right.right is None:
              min_node_of_right.parent.left=None
           else:
              min_node_of_right.parent.left=min_node_of_right.right
           return
                  
# если 2 ребенка
        if (node.left is not None) and (node.right is not None):
            min_node_of_right=self.find_min_node(node.right)
            min_node_of_right.left=node.left
            if node.parent.left==node:
               node.parent.left=min_node_of_right
            else:
               node.parent.right=min_node_of_right
            return
        
        raise Exception("Что то пошло не так")


bst=BinarySearchTree()

bst=BinarySearchTree()
a=[1,2,3,4,5,6,7,8,9,10]
bst.add_sort_list(a)
#bst.add(5)
#bst.add(3)
#bst.add(1)
#bst.add(2)
#bst.add(8)
#bst.add(7)
#bst.add(6)
#bst.add(19)
#bst.add(15)
#bst.add(22)
#bst.add(6.5)
#bst.delete(5)
a=10