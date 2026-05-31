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




