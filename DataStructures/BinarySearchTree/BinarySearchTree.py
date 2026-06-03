class Node:

    def __init__(self,data,parent=None):

        self.data = data
        self.left_node = None
        self.right_node = None
        #usefull when implement the remove function
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        #we can access the root node execulsively
        self.root = None


    def remove(self,data):

        if self.root:
            self.remove_node(data,self.root)


    def remove_node(self,data,node):
        #first we have find which node to remove

        if node is None:
            return
        
        if data < node.data:

            self.remove_node(data,node.left_node)


        elif data > node.data:
        
            self.remove_node(data,node.right_node)

        else:

            #we have found the node to remove
            #there are 3 options
            #leaf node case
            if node.left_node is None and node.right_node is None:
                print("Removing the leaf node %d" % node.data)
                parent = node.parent
                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None  
                del node

            #when there is a single child
            elif node.left_node is None and node.right_node is not None:
                print("Removing a node with sigle right child %d" % node.data)
                parent = node.parent

                if parent is not None and parent.left_node == node:

                    parent.left_node = node.right_node

                if parent is not None and parent.right_node == node:
                    
                    parent.right_node = node.right_node

                if parent is None:
                    self.root = None  

                node.right_node.parent = parent
                del node


    def insert(self,data):

        #if first node
        if self.root is None:
            self.root = Node(data)

        else:

            self.insert_node(data,self.root)

    def insert_node(self,data,node):

        #we have go to left subtree

        if data < node.data:
            if node.left_node:
                # the left node exists (so we keep going)
                self.insert_node(data,node.left_node)
            else:
                #there is no left node(so we create one)
                node.left_node = Node(data,node)
        #we have to go the right subtree
        else:
            if node.right_node:
                # the right node exists (so we keep going)
                self.insert_node(data,node.right_node)
            else:

                #there is no right node(so we create one)
                node.right_node = Node(data,node)


    def get_min(self):
        if self.root:
            return self.get_min_value(self.root)

    def get_min_value(self,node):

        if node.left_node:
            return self.get_min_value(node.left_node)
        #return the left most item that is min vale
        return node.data
    

    def get_max(self):
        if self.root:
            return self.get_max_value(self.root)

    def get_max_value(self,node):

        if node.right_node:
            return self.get_max_value(node.right_node)
        #return the RIGHT most item that is mAX vale
        return node.data
    

    def traverse(self):

        if self.root:
            return self.traverse_in_order(self.root)


    #it has O(N) linera running time complexity
    def traverse_in_order(self,node):

        if node.left_node:
            self.traverse_in_order(node.left_node)

        print(node.data)

        if node.right_node:
            self.traverse_in_order(node.right_node)



if __name__ == '__main__':

    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(9)
    bst.insert(8)
    bst.insert(6)
    bst.insert(7)
    bst.insert(11)
    bst.insert(12)
    bst.insert(-5)

    bst.traverse()

    print("max value",bst.get_max())
    print("min value",bst.get_min())












