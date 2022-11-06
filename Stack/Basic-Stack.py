class Stack:
    def __init__(self, max_size):
        self.top_pointer = -1
        self.length = max_size
        self.stack = [None for x in range(max_size)]

    def push(self, new_element):
        self.top_pointer = self.top_pointer + 1
        if self.length > self.top_pointer:
            self.stack[self.top_pointer] = new_element
        else:
            print('Stack overflow...')

    def pop(self):
        if self.top_pointer < 0:
            return 'Stack underflow'
        last_element = self.stack[self.top_pointer]
        self.stack[self.top_pointer] = None
        self.top_pointer = self.top_pointer - 1
        return last_element

    def peek(self):
        return self.stack[self.top_pointer-1]

    def is_empty(self):
        return self.top_pointer == -1

    def print_stack(self):
        print(f'Stack Now : {self.stack}')


stack = Stack(5)

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.print_stack()

# print(stack.peek())

print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.print_stack()
print(stack.pop())


# stack.push(60)
# stack.print_stack()
# stack.push(70)
# stack.print_stack()
# stack.push(80)
# stack.print_stack()
# stack.push(90)
# stack.print_stack()
