from Stack import Stack

stackofDocuments = Stack()
stackofDocuments.push(1)

stackofDocuments.push(2)

stackofDocuments.push(8)

stackofDocuments.push(3)

stackofDocuments.push(7)

stackofDocuments.push(5)

stackofDocuments.push(4)

# Do not modify code above

documentsList = [] # create a list
while not stackofDocuments.isEmpty(): # empty the stack and add each item to the list
        documentsList.append(stackofDocuments.pop()) 

sortedList = sorted(documentsList) # sort the list of documents
for i in sortedList: 
    stackofDocuments.push(i)# put the items back in the stack

stackofDocuments.printStack() # print the stack



