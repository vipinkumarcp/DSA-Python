

#LIFO METHOD - last in,first out method

class Stack:

    def __init__(self):
        self.stack = []  #stack is 1d array

        #implementing push method insert item in stack
    def push(self,data):
        self.stack.append(data)

        #remove and return the last item we have inserted

    #O(1) cosntant time running complixity
    def pop(self):
        data = self.stack[-1]  #this synstax return last item in array
        del self.stack[-1]   #remove last stack
        return data
        
    #retrun last item

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)


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
print(stack.stack.peek())








