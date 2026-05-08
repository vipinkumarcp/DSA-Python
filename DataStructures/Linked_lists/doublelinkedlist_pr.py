class Node:
    def __init__(self,data):

        self.data = data
        self.prev_node = None
        self.next_node = None

    def __repr__(self):
        return str(self.data)


class DoubleLinkedList:


    def __init__(self):
        self.head = None
        self.tail = None
        self.no_of_nodes = 0


    def insert(self,data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:

            new_node.prev_node = self.tail
            self.tail.next_node = new_node
            self.tail = new_node


        
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:

            print(actual_node)
            actual_node = actual_node.next_node

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:

            print(actual_node)
            actual_node = actual_node.prev_node



if __name__ == '__main__' :
    linked_list = DoubleLinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)

    linked_list.traverse_forward()
    print('------------------------')
    linked_list.traverse_backward()