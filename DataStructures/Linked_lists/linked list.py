class Node:
    # nodes are connected with edge
    def __init__(self, data):
        self.data = data
        self.nextNode = None  # every single node is refering the next node

    # O(1) running complixity


class LinkedList:

    def __init__(self):
        self.head = None  # head node is the first node of linked list
        self.numOfNodes = 0  # at beggining it is zero

    def insert_start(self, data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)  # instantiate new node

        if not self.head:  # check head node none or not(to check whether it is first node)
            self.head = new_node
        else:  # if link list is not empty
            new_node.nextNode = self.head
            self.head = new_node  # reinstialize self node to new node

    # running time complexity O(N)
    def insert_end(self, data):
        self.numOfNodes = self.numOfNodes + 1  # increment size of link list
        new_node = Node(data)  # instantiate new node
        actual_node = self.head
        # to find last node
        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode  # actual node last node of linked list

        actual_node.nextNode = new_node

    def remove(self, data):
        # link list is empty does't contain any item
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None  # at begining

        while actual_node is not None and actual_node.data != data:  # to avoid infinte loop #serach item
            previous_node = actual_node
            actual_node = actual_node.nextNode

        # serach miss - the item is not in linked list
        if actual_node is None:
            return
        self.numOfNodes = self.numOfNodes - 1

        #update the refernces(so we have the data we want to remove
        #the head node is one we want to remove 
        if previous_node is None:
            self.head = actual_node.nextNode
        else:
            #remove an internal node by updating the points
            # no need to del the node beacause the garbage collector will do that
            previous_node.nextNode = actual_node.nextNode

    # size of linked list
    # O(1)running complexity
    def sizeOfList(self):
        return self.numOfNodes

    # to print values of link list
    # O(N) to consider all nodes
    def traverse(self):

        actual_node = self.head

        # to check it is last node

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.nextNode


linked_list = LinkedList()
linked_list.insert_start(4)
linked_list.insert_start(3)
linked_list.insert_start(7)
linked_list.insert_end(18)
linked_list.insert_end(18)
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
