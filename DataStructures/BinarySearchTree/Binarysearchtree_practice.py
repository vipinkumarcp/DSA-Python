class Node:

    def __init__(self,data,parent=None):
        self.data = data
        self.parent = parent
        self.right_node = None
        self.left_node = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:

            self.root = Node(data)

        else:

            self.insert_node(data,self.root)

    
    def insert_node(self,data,node):

        if data < node.data:

            if node.left_node:

                self.insert_node(data,node.left_node)

            else:
                node.left_node = Node(data,node)

        else:

            if node.right_node:

                self.insert_node(data,node.right_node)
            else:

                node.right_node = Node(data,node)


    def traverse(self):

        if self.root:
            return self.traverse_inorder(self.root) 
        
    def traverse_inorder(self,node):

        if node.left_node:
            self.traverse_inorder(node.left_node)
        
        print(node.data)

        if node.right_node:
            self.traverse_inorder(node.right_node)
       

    def max(self):

        if self.root:

            return self.get_max(self.root)
        
    def get_max(self,node):

        if node.right_node:

            return self.get_max(node.right_node)

        return node.data
    



if __name__ == '__main__':


    bst = BinarySearchTree()

    bst.insert(4)
    bst.insert(10)
    bst.insert(-2)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)
    bst.insert(8)
    bst.insert(2)

    bst.traverse()
    print("max",bst.max())



