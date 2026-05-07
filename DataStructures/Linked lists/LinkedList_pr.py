class Node:

    def __init__(self,data):

        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):

        self.no_of_nodes = 0
        self.head = None

    def insert_start(self,data):

        self.no_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_end(self,data):

        self.no_of_nodes += 1
        new_node = Node(data)

        actual_node = self.head

        while actual_node.next_node is not None:

            actual_node = actual_node.next_node

        actual_node.next_node = new_node


    def remove(self,data):

        actual_node = self.head
        previous_node = None

        while actual_node is not None  and actual_node.data != data:

            previous_node = actual_node
            actual_node = actual_node.next_node

        if actual_node is None:

            return

        self.no_of_nodes -= 1

        if previous_node == None:

            self.head = actual_node.next_node

        else:
           
            
            previous_node.next_node = actual_node.next_node

    
    def sizeOfList(self):
        return self.no_of_nodes
    

    def traverse(self):

        actual_node = self.head

        while actual_node is not None:

            print(actual_node)
            actual_node = actual_node.next_node

       



linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
linked_list.insert_end(18)
linked_list.insert_end(10)
linked_list.insert_start('Adam')
linked_list.traverse()
print('size:', linked_list.sizeOfList())
print('//////////////')
linked_list.remove('Adam')
linked_list.traverse()
print('size', linked_list.sizeOfList())
print('//////////////')
linked_list.remove(10)
linked_list.traverse()
linked_list.traverse()













    