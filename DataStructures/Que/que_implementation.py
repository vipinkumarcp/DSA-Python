
class Queue:

    def __init__(self):
        self.queue = []


    def enqueue(self,data):

        self.queue.append(data)


    def dequeue(self):

        data = self.queue[0]

        del self.queue[0]

        return data
    
    def peek(self):

       
        return self.queue[-1]
    
    def que_size(self):

        return len(self.queue)
    
    def is_empty(self):

        if len(self.queue) < 1:

            return -1


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.que_size())
print(queue.dequeue())
print(queue.que_size())
