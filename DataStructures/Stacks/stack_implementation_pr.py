
class Stack:

    def __init__(self):
        
        self.stack = []


    
    def push(self,data):
        self.stack.append(data)


    def pop(self):

        data = self.stack[-1]

        del data

        return data
    
    def peek(self):

       
        return self.stack[-1]
    
    def stack_size(self):

        return len(self.stack)
    
    def is_empty(self):

        if len(self.stack) < 1:

            return -1

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("size of stack {}".format(stack.stack_size()))
print("popped item {}".format(stack.stack.pop()))
print("size of stack {}".format(stack.stack_size()))
print("popped item {}".format(stack.stack.pop()))
print("size of stack {}".format(stack.stack_size()))
