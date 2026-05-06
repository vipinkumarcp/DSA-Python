class Node:

    def __init__(self,data):

        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):

        self.no_of_nodes = 0
        self.head = None

    def insert_node(self,data):

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















    