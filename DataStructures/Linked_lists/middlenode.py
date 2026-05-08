class Node:

    def __init__(self,data):

        self.data =  data
        self.next_node = None



class LinkedList:


    def __init__(self):

        self.head = None


    def insert(self,data):

        new_node =  Node(data)

        if self.head is None:

            self.head = new_node

        else:

            new_node.next_node = self.head
            self.head = new_node


    def middle_node(self):

        slow_pointer = self.head
        fast_pointer = self.head

        while fast_pointer and fast_pointer.next_node:
            slow_pointer = slow_pointer.next_node
            fast_pointer = fast_pointer.next_node.next_node

        return slow_pointer
    

    def traverse(self):

        actual_node = self.head

        while actual_node:

            print(actual_node.data)
            actual_node = actual_node.next_node





linkedlist = LinkedList()

for i in range(6,0,-1):
    linkedlist.insert(i)


linkedlist.traverse()
print("*****************")
middle = linkedlist.middle_node()
print(middle.data)
