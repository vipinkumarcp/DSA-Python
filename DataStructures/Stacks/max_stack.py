class MaxStack:

    def __init__(self):
        self.main_stack = []
        self.max_stack = []


    def push(self,data):



        self.main_stack.append(data)

        if (len(self.main_stack) ==1):
            self.max_stack.append(data)
            return
        
        if data > self.max_stack[-1]:
            self.max_stack.append(data)

        else:
            self.max_stack.append(self.max_stack[-1])
        

    def pop(self):

        data = self.main_stack[-1]

        del self.main_stack[-1]
        del self.max_stack[-1]

        return data
    
   
    

    def max_item(self):

        return self.max_stack[-1]
    

    def len_max_stack(self):

        return len(self.max_stack)
    

    def len_main_stack(self):
        return len(self.main_stack)

    def print_stack(self):
        print("Stack contents:", self.main_stack)
        if self.max_stack:
            print("Current max:", self.max_stack[-1])
        else:
            print("Stack is empty.")


if __name__ == "__main__":
    stack = MaxStack()
    values = [3, 5, 2, 10, 7]
    for value in values:
        stack.push(value)
    stack.print_stack()
    print("Stack size:", stack.len_main_stack())
    print("Max item:", stack.max_item())

    
    
    
    


    