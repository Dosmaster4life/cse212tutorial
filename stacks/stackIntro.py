import Stack
    
stack = Stack()
stack.push('a') # add item to stack, also known as push
stack.push('b')
stack.push('c')
stack.push('d')

print("---Original Stack---") #stack with a, b, c, d
print(stack.printStack())

print("---Top of the stack---") #stack with a, b, c, d
stack.peek()# view the top item of the stack

stack.pop() # remove top item from the stack which is d

print("---Stack with top removed---")
print(stack.printStack()) # stack with a, b, c

stack.pop() 
stack.pop()
stack.pop()
print("---Empty Stack---")
print(stack.printStack())
