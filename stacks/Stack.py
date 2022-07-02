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
    if not isEmpty():
      print(self.stack[len(self.stack) - 1])

    def isEmpty(self): # Check if the stack is empty
      if len(self.stack) >= 0:
         return False
      else:
         return True

   def printStack(self): # print all items in the stack, not native to a stack typically
      for stackItem in reversed(self.stack):
        print(stackItem)
