
class Node:

    def __init__(self,data):
        self.data = data
        self.next_node =None


class LinkedList:

    def __init__(self):
        self.head = None
        self.no_of_nodes = None

    
    def insert_start(self,data):

        new_node = Node(data)

        if not self.head:

            self.head = new_node
        else:

            new_node.next_node = self.head
            self.head = new_node


    def insert_end(self,data):

        new_node = Node(data)

        actual_node = self.head

        while actual_node.next_node is not None:

            actual_node = actual_node.next_node

        actual_node.next_node = new_node


    def remove(self,data):

        actual_node = self.head

        previous_node = None

        while actual_node.next_node is not None and actual_node.data != data:

            previous_node = actual_node

            actual_node = actual_node.next_node

        if previous_node is None:

            self.head = actual_node.next_node

        else:

            previous_node.next_node = actual_node.next_node


    def middle_node(self,data):

        fast_pointer = self.head

        slow_pointer = self.head

        while fast_pointer and fast_pointer.next_node:

            slow_pointer = slow_pointer.next_node

            fast_pointer = fast_pointer.next_node.next_node

        return slow_pointer






        



        

