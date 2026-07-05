class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None
        self.previous_node = None


class LRUcache:

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("capacity must be greater than 0")

        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next_node = self.tail
        self.tail.previous_node = self.head

    def insert(self, newnode):
        temp = self.head.next_node
        newnode.previous_node = self.head
        newnode.next_node = temp
        self.head.next_node = newnode
        temp.previous_node = newnode

    def remove(self, delnode):
        prev = delnode.previous_node
        nxt = delnode.next_node

        if prev is not None:
            prev.next_node = nxt
        if nxt is not None:
            nxt.previous_node = prev

        delnode.previous_node = None
        delnode.next_node = None

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]

        if len(self.cache) >= self.capacity:
            lru_node = self.tail.previous_node
            if lru_node is not self.head:
                self.remove(lru_node)
                del self.cache[lru_node.key]

        newnode = Node(key, value)
        self.insert(newnode)
        self.cache[key] = newnode




    





        







        
        