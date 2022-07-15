from Stack import Stack

stackofDocuments = Stack()

stackofDocuments.push("Important document number 1")

stackofDocuments.push("Important document number 2")

stackofDocuments.push("Important document number 3")

stackofDocuments.push("Important document number 4")

stackofDocuments.push("Important document number 5")


def putAtBotton(stackOfDocs, document):
   if stackOfDocs.isEmpty():
         stackOfDocs.push(document) # Put first item in stack
   else:
      documentPopped = stackOfDocs.pop() # pop the original and store it
      putAtBotton(stackOfDocs,document) # Recursivly go through each document
      stackOfDocs.push(documentPopped) # Put the next item in the stack


def reverseStack(stackofDocs): 
   if stackofDocs.isEmpty():
      return
   else:
      documentPopped = stackofDocs.pop()  # pop the original and store it it
      reverseStack(stackofDocs) # Recursivly go through each item in the stack
      putAtBotton(stackofDocs,documentPopped) # put the items in reverse order through this
      

print("---Original Stack---")
stackofDocuments.printStack() # original stack
reverseStack(stackofDocuments) 
print("---Reversed Stack---")
stackofDocuments.printStack() # reversed stack


   
