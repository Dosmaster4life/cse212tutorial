class Stack:
   def __init__(self):
      self.stack = [] #create the stack(this is a list)

   def push(self, value):
      self.stack.append(value) # add an item to the stack
        

   def pop(self):
      if len(self.stack) > 0:
         return self.stack.pop() # Use remove the top item from the stack
      else:
        return "stack is empty."
    
   def peek(self): # view the top item of the stack
    if len(self.stack) > 0:
      print(self.stack[len(self.stack) - 1])

   def printStack(self): # print all items in the stack
      for stackItem in reversed(self.stack):
        print(stackItem)

