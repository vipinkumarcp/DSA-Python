#Construct an in-place algorithm to reverse a linked list!


class Node:

    def __init__(self,data):

        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):

        self.head = None
        self.no_of_nodes = 0


    
    def insert(self,data):

        new_node = Node(data)

        if self.head is None:

            self.head = new_node

        else:

            new_node.next_node = self.head

            self.head = new_node



    def reverse(self):

        current_node = self.head
        previous_node = None
        next_node = None

        while current_node:

            next_node = current_node.next_node
            current_node.next_node = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node


    def traverse(self):

        current = self.head

        while current:
            print(current.data)
            current = current.next_node


linked_list = LinkedList()

linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)

linked_list.traverse()
print("***********************")
linked_list.reverse()
linked_list.traverse()
print("***********************")
        
        
